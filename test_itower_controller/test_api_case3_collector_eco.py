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

@pytest.mark.repeat(5)
@pytest.mark.http_api_itower_controller
def test_http_api_eco_switch():
    """
        控制器节能开/关控制
        1. 遍历设备列表,过滤采集器类设备，收集设备ID
        2. 查询节能当前状态
        3. 设置与1查询结果相反的状态
        4. 查询节能当前状态是否与步骤2设置的状态相同
    """
    
    collectorList = slave_mgr_collector_list()
    assert collectorList != None

    print('\n')
    for item in collectorList:
        count:int = 2
        expectedEcoSt:bool = False
        while count > 0:
            sId:int = item['id']
            ecoStIsOn = slave_mgr_is_eco_on( sId ); time.sleep(2) # 读取采集器当前的节能状态        
            if ecoStIsOn==True: expectedEcoSt = False
            else: expectedEcoSt = True
            slave_mgr_eco_st_set(sId, expectedEcoSt); time.sleep(2)
            ecoStIsOn = slave_mgr_is_eco_on( sId ) # 读取采集器当前的节能状态
            assert ecoStIsOn==expectedEcoSt
            time.sleep(2)
            count-=1

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