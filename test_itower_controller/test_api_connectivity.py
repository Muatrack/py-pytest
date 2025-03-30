import pytest
import requests
# import responses_validator
import time
from itower_http_api_lib import *
from itower_http_api_wrapper import *


"""
用例说明

1 子设备增删改查
2 分合闸
    2.1  自动搜索
    2.2  对采集器发起分合闸测试
3 开关机 ???

"""


'''
预定义值
    测试环境温度1
    测试环境温度2
    测试空调1
    测试空调1回风1
    测试空调2
    测试空调2回风1
    测试人体
'''
newSlvList=[
                {'sn':'9128B28507570001', 'name':'5rWL6K+V546v5aKD5rip5bqmMQ=='},
                {'sn':'9128B28507570002', 'name':'5rWL6K+V546v5aKD5rip5bqmMg=='},
                {'sn':'170902FB2340E001', 'name':'5rWL6K+V56m66LCDMQ=='},
                {'sn':'9128B28507570003', 'name':'5rWL6K+V56m66LCDMeWbnumjjjE='},
                {'sn':'170902FB2340E002', 'name':'5rWL6K+V56m66LCDMg=='},
                {'sn':'9128B28507570004', 'name':'5rWL6K+V56m66LCDMuWbnumjjjE='},
                {'sn':'910102FA2340A000', 'name':'5rWL6K+V5Lq65L2T'}
]

collectorStrKey:str = "WSCK"

# 预定义值

def http_api_1_5_sw_on(id:int):
    """
        合闸封装
    """
    http_api_1_5(id, Api5CtlCls.SW_ON)

def http_api_1_5_sw_off(id:int):
    """
        分闸封装
    """
    http_api_1_5(id, Api5CtlCls.SW_OFF)

def http_api_1_5_air_on(id:int):
    """
        空调机开机封装
    """
    http_api_1_5(id, Api5CtlCls.AIR_ON)

def http_api_1_5_air_off(id:int):
    """
        空调机关机封装
    """
    http_api_1_5(id, Api5CtlCls.AIR_OFF)

#------------------------------------------------------------------------------------------------------#

# @pytest.mark.repeat(10)
@pytest.mark.http_api_itower_controller
def test_http_api_all():
    """
        全部HTTP API调用一次

        检查请求的连通性，仅检查http api的相应值
    """
    
    http_api_1_1(); time.sleep(2)                       # 查询设备列表
    # http_api_1_2(); time.sleep(2)                       # 查询设备的采集数据


@pytest.mark.repeat(1)
@pytest.mark.http_api_itower_controller
def test_http_api_slave_query():
    """ 查询设备
        :return 子设备数组:
    """
    resp = http_api_1_1()
    assert resp.status_code==200
    body = resp.json()
    assert body['code']==1000
    time.sleep(1)
    return None


@pytest.mark.repeat(1)
@pytest.mark.http_api_itower_controller
def test_http_api_slave_crud():
    """ 设备增、删、改、查
        1. 查: 查询设备列表
        2. 删: 删除1中所有的设备, 确保控制器已存在设备的状态
        3. 增: 增加设备，名称使用 newSlvList 定义
        4. 查询设备列表，对比设备数量与3中增加设备数量是否一致
    """
    fakeSlave:dict = {
        'name': '5rWL6K+V5pS55Y+Y5ZCN56ew',
        'pid': 2
    }
    
    resp = http_api_1_1()
    assert resp.status_code==200
    body = resp.json()
    assert body['code']==1000
    slvIdList:list = []
    originList:list = body['data']['list']
    originCount:int = body['data']['count']
    
    print('\n')
    for item in originList:
        slvIdList.append( item['id'] )
    # 删除所有查询到的设备
    if len(slvIdList) > 0:
        respCode = http_api_1_4(slvIdList)
        print('Invoke slave del, resp code:', respCode)
    else:
        print("slave list is empty")
        print(originList, ' len:', len(originList))

    time.sleep(1)
    # 此处检查，设备数量应为0
    resp = http_api_1_1()
    assert resp.status_code==200
    originList:list = resp.json()['data']['list']
    assert len(originList)==0

    # 新增设备
    for item in newSlvList:
        # print("name:%s, sn:%s", {item['name'], item['sn']})
        respCode = http_api_1_3( item['name'], item['sn'] )
        assert respCode==1000
        time.sleep(2)
    # 验证新增结果。先读取子设备列表，验证条目数量，验证全部子设备的sn
    resp = http_api_1_1()
    assert resp.status_code==200
    originList:list=resp.json()['data']['list']
    # 验证子设备数量，应与 newSlvList 数据
    assert len(originList)==len(newSlvList) # 验证子设备数量
    bFoundSN:bool = False
    for item in originList:
        bFoundSN=False
        for ia in newSlvList:
            if item['sn'].lower()==ia['sn'].lower():
                bFoundSN=True
        # 查询到的设备列表，应当与预设列表sn相等
        assert bFoundSN==True

    # 修改设备(sid=1)名称为 changedName
    respData:object = http_api_1_6(1,{'name':fakeSlave['name'], 'pid':fakeSlave['pid']})
    assert respData['code']==1000
    time.sleep(1)
    # 读取设备列表，找到id==1的设备信息，将其name 与 changedName 比较，相等时表示成功
    resp = http_api_1_1()
    assert resp.status_code==200
    originList:list=resp.json()['data']['list']
    for item in originList:
        if (item['id']==1):
           assert item['name']==fakeSlave['name']
           assert item['pid']==fakeSlave['pid']

@pytest.mark.repeat(1)
@pytest.mark.http_api_itower_controller
def test_http_api_discovery():
    """ 发现周边设备, 发现设备完毕后延迟30s, 给发现功能留出足够的运行时间
        1. 删除所有一存在的设备
        2. 开启发现周边设备
    """
    # 删除所有设备
    slave_mgr_delete_all(); time.sleep(10)
    # 执行自动搜索
    slave_mgr_discovery();  time.sleep(30)


@pytest.mark.repeat(3)
@pytest.mark.http_api_itower_controller
def test_http_api_power_switch():
    """ 分合闸循环, 测试环境中存在异常的采集器 sn:170902fb2399036d， 将其排除
        1. 查询设备列表
        2. 对采集器实施循环分合闸
    """
    print('\n')
    # 查询设备
    slvCnt, slvList = slave_mgr_list_query()
    assert slvCnt>0
    collectorList:list = []
    # 遍历列表，过滤出采集器的id，并装入列表 collectorList
    for item in slvList:
        if collectorStrKey in item['model']:
            collectorList.append({'id':item['id'],'sn':item['sn']})
    assert len(collectorList)>0
    durationTs:int = 6
    # 遍历 id list, 发送分合闸、开关机控制
    for item in collectorList:
        sId:int = item['id']

        if '170902fb2399036d'.lower()==item['sn'].lower(): break             # 排除异常的sn设备

        print(item['sn'],' ', item['id'], '----- sw off')
        http_api_1_5_sw_off(sId); time.sleep(durationTs)     # 发起分闸
        # 查询子设备采集数据，过滤开关状态
        swSt = slave_mgr_is_sw_on(sId); time.sleep(2)
        # assert swSt==False
        print(item['sn'],' ', item['id'], '----- sw on')            
        http_api_1_5_sw_on(item['id']); time.sleep(durationTs)      # 发起合闸            
        # assert swSt==True

'''
@pytest.mark.repeat(10)
@pytest.mark.http_api_itower_controller
def test_http_api_ac_switch():
    """
        开关机循环
        1. 删除所有设备
        2. 执行设备搜索、自动添加
        3. 查询设备列表
        4. 循环分合闸
    """

    # 删除所有设备
    slave_mgr_delete_all(); time.sleep(10)
    # 执行自动搜索
    slave_mgr_discovery();  time.sleep(30)
    # 查询设备
    slvCnt, slvList = slave_mgr_list_query()
    assert slvCnt>0

    collectorList:list = []
    # 遍历列表，过滤出采集器的id，并装入列表 collectorList
    for item in slvList:
        if collectorStrKey in item['model']:
            collectorList.append({'id':item['id'],'sn':item['sn']})
    assert len(collectorList)>0

    durationTs:int = 6    
    # 遍历 id list, 发送分合闸、开关机控制
    for item in collectorList:
        performCounter = 10
        while performCounter > 0:
            sId:int = item['id']
            print(item['sn'],' ', item['id'], '----- ac off')
            http_api_1_5_air_off(item['id']); time.sleep(durationTs)    # 发起开机
            print(item['sn'],' ', item['id'], '----- ac on')
            http_api_1_5_air_on(item['id']); time.sleep(durationTs)     # 发起关机
            performCounter-=1


@pytest.mark.repeat(10)
@pytest.mark.http_api_itower_controller
def test_http_api_ac_switch():
    """
        空调开关机循环

        依赖 test_http_api_slave_query 查询结果
        遍历列表中属于采集器的类型设备，进行分合闸控制
    """
    pass

@pytest.mark.repeat(10)
@pytest.mark.http_api_itower_controller
def test_http_api_slave_del():
    """
        删除设备

        依赖 test_http_api_slave_add 增加的设备
        记录、对比 操作前后的设备数量的变化、操作前后设备id对比、判定操作是否成功
    """
    pass

@pytest.mark.repeat(10)
@pytest.mark.http_api_itower_controller
def test_http_api_slave_mod():
    """
        修改设备

        执行查询设备列表，对指定id修改名称，再次查询设备列表读取指定id设备的名称，对比查询到的name与修改时写入的name是否相同
    """
    pass

@pytest.mark.repeat(10)
@pytest.mark.http_api_itower_controller
def test_http_api_ctler_fwver():
    """
        读取控制器的固件版本
    """
    pass

@pytest.mark.repeat(10)
@pytest.mark.http_api_itower_controller
def test_http_api_ctler_ota():
    """
        控制器升级
    """
    pass

'''