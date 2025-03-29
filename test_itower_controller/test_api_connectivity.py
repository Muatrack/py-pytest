import pytest
import requests
# import responses_validator
import time
from itower_http_api_lib import *

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
    http_api_1_2(); time.sleep(2)                       # 查询设备的采集数据
    # 增加设备，名称：自动添加设备， SN：170902FB23DDEEFF
    # http_api_1_3(name="6Ieq5Yqo5re75Yqg6K6+5aSH", sn="170902FB23DDEEFF"); time.sleep(2)

    # http_api_1_6(destSlaveId, {"name":"base64"}); time.sleep(2)     # 修改子设备名称
    # http_api_1_6(destSlaveId, {"pid":0}); time.sleep(2)             # 修改子设备父id

@pytest.mark.repeat(1)
@pytest.mark.http_api_itower_controller
def test_http_api_slave_query():
    """
        查询设备

        :return 子设备数组:
    """
    resp = http_api_1_1()
    assert resp.status_code==200
    body = resp.json()
    assert body['code']==1000


@pytest.mark.repeat(1)
@pytest.mark.http_api_itower_controller
def test_http_api_slave_curd():
    """
        设备增、删、改、查

        1 查: 查询设备列表
        2 删: 删除1中所有的设备, 确保控制器已存在设备的状态
        3 增: 增加设备，名称使用 newSlvList 定义
        4 查询设备列表，对比设备数量与3中增加设备数量是否一致
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
        time.sleep(1)
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


'''
@pytest.mark.repeat(10)
@pytest.mark.http_api_itower_controller
def test_http_api_power_switch():
    """
        分合闸循环
        
        依赖 test_http_api_slave_query 查询结果
        遍历列表中属于采集器的类型设备，进行分合闸控制
    """
    durationTs = 3
    repeatCount = 10
    while( repeatCount>0 ):
        destSlaveId = 11
        http_api_1_5_sw_off(destSlaveId); time.sleep(durationTs)     # 发起分闸
        http_api_1_5_sw_on(destSlaveId); time.sleep(durationTs)      # 发起合闸
        http_api_1_5_air_off(destSlaveId); time.sleep(durationTs)    # 发起开机
        http_api_1_5_air_on(destSlaveId); time.sleep(durationTs)     # 发起关机

        destSlaveId = 13
        http_api_1_5_sw_off(destSlaveId); time.sleep(durationTs)     # 发起分闸
        http_api_1_5_sw_on(destSlaveId); time.sleep(durationTs)      # 发起合闸
        http_api_1_5_air_off(destSlaveId); time.sleep(durationTs)    # 发起开机
        http_api_1_5_air_on(destSlaveId); time.sleep(durationTs)     # 发起关机

        destSlaveId = 18
        http_api_1_5_sw_off(destSlaveId); time.sleep(durationTs)     # 发起分闸
        http_api_1_5_sw_on(destSlaveId); time.sleep(durationTs)      # 发起合闸
        http_api_1_5_air_off(destSlaveId); time.sleep(durationTs)    # 发起开机
        http_api_1_5_air_on(destSlaveId); time.sleep(durationTs)     # 发起关机

        repeatCount-=1


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