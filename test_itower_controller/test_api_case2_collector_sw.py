import pytest
import requests
# import responses_validator
import time
from itower_http_api_lib import *
from itower_http_api_wrapper import *


"""
用例说明
    采集器分合闸测试
        - 自动搜索
        - 对采集器发起分合闸测试

"""

#------------------------------------------------------------------------------------------------------#

# @pytest.mark.repeat(50)
@pytest.mark.http_api_itower_controller
def test_http_api_power_switch():
    """ 分合闸循环, 测试环境中存在异常的采集器 sn:170902fb2399036d， 将其排除
        1. 查询设备列表
        2. 对采集器实施循环分合闸
    """
    print('\n')
    # 查询设备
    collectorList = slave_mgr_collector_list()
    assert collectorList != None
    durationTs:int = 6
    # 遍历 id list, 发送分合闸、开关机控制
    for item in collectorList:
        sId:int = item['id']
        runTimes:int = 2
        expectedSwSt:bool = False

        while runTimes>0:
            # 查询状态
            swSt = slave_mgr_is_pow_on(sId); time.sleep(2)
            if swSt==True: expectedSwSt=False
            else: expectedSwSt = True
            # 设置分合闸
            print(">>>>>>>>>> ", str(expectedSwSt))
            slave_mgr_power_st_set(sId, expectedSwSt)
            time.sleep(5)
            # 查询、验证电闸状态
            print("<<<<<<<<<< ", str(expectedSwSt))
            swSt = slave_mgr_is_pow_on(sId)
            assert swSt==expectedSwSt
            time.sleep(1)
            runTimes-=1

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