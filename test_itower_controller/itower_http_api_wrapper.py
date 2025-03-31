from itower_http_api_lib import *
import time

collectorStrKey:str     = "WSCK"
collector2pKey:str      = ""
collector3pKey:str      = ""

def slave_mgr_list_query():
    ''' 查询设备列表
        :return int, list: 设备数量，设备列表
    '''
    resp = http_api_1_1()
    assert resp.status_code==200
    body = resp.json()
    assert body['code']==1000    
    originList:list = body['data']['list']
    originCount:int = body['data']['count']
    return originCount, originList

def slave_mgr_collector_list()->list|None:
    ''' 查询采集器列表
        :return int, list: 设备数量，设备列表
    '''
    collectorList:list = []
    slvCnt,slvList=slave_mgr_list_query()
    if slvCnt<1:
        return None
    for item in slvList:
        if (collectorStrKey in item['model']) and ('170902fb2399036d'.lower()!=item['sn'].lower()):
            collectorList.append( item )
    if len(collectorList)>0: return collectorList
    else: return None


def slave_mgr_data_query(sId:int):
    """ 查询子设备的采集数据
        :param sId: 子设备id
        :param Object: 返回查询到的子设备数据
    """
    dataResp:object = http_api_1_2()
    return dataResp

def _slave_mgr_control_status(dataIn:object)->tuple[bool,bool,bool,bool]|None:
    """ 判断采集器多种控制功能的状态

        :param data: 读取的子设备采集信息object
        :return tuple[]: [0]节能模式T/F, [1]压缩机运行T/F, [2]开关机T/F, [3]分合闸T/F
    """
    # 判断采集器类型 2p/3p | "ECO=1, RUN=0, ON=0, POW=1"
    assert collectorStrKey in dataIn['model'] and "values" in dataIn
    if 'STA' not in dataIn['values']:
        return None
    strArray=dataIn['values']['STA'].split(",")
    assert len(strArray)==4
    ecoSt:str = strArray[0].split("=")[1]
    runSt:str = strArray[1].split("=")[1]
    onSt:str  = strArray[2].split("=")[1]
    powSt:str = strArray[3].split("=")[1]

    return ecoSt=='1',runSt=='1',onSt=='1',powSt=='1'


def slave_mgr_is_pow_on(sId:int)->bool|None:
    """ 判断采集器的电闸是否合闸状态
        :param data: 读取的子设备采集信息object
        :return: 0-节能模式T/F, 1-压缩机运行T/F, 2-开关机T/F, 3-分合闸T/F
    """
    # 发起请求, 读取子设备的采集数据
    respData:object = http_api_1_2(sId)
    ctrlStatus=_slave_mgr_control_status(respData)
    if ctrlStatus==None: return None
    else: return ctrlStatus[3]

def slave_mgr_is_eco_on(sId:int)->bool|None:
    """ 读取采集器节能控制当前的状态
        :param data: 读取的子设备采集信息object
        :return: 1-节能开启，0-节能关闭
    """
    # 发起请求, 读取子设备的采集数据
    respData:object = http_api_1_2(sId)
    ctrlStatus=_slave_mgr_control_status(respData)
    if ctrlStatus==None: return None
    else: return ctrlStatus[0]

def slave_mgr_delete_all():
    '''
        删除所有设备
        1. 读取设备列表
        2. 依次删除
        3. 再次读取设备列表，验证设备数量
    '''
    
    slvCount, slvList = slave_mgr_list_query()
    # 设备数量为0, 不需删除
    if slvCount==0: return
    
    # 遍历设备list, 依次删除

    print('\n')
    slvIdList:list = []
    # 将所有设备的id 装入 list
    for item in slvList:
        slvIdList.append( item['id'] )
    # 删除所有查询到的设备
    assert len(slvIdList)>0
    respCode = http_api_1_4(slvIdList)
    assert respCode==1000
    time.sleep(1)

def slave_mgr_discovery():
    """ 请求控制器自动发现周边设备 """
    http_api_3_1()

def slave_mgr_eco_st_set(sId:int, sw:bool):
    """ 采集器节能开启/关闭
        :param sId: 子设备id
        :param sw:  True-开启节能，False-关闭节能
    """
    if sw==True: http_api_1_5(sId, Api5CtlCls.ECO_ON)
    else: http_api_1_5(sId, Api5CtlCls.ECO_OFF)

def slave_mgr_power_st_set(sId:int, sw:bool):
    """ 采集器电闸连通/断开
        :param sId: 子设备id
        :param sw:  True-连通电闸，False-断开电闸
    """
    if sw==True: http_api_1_5(sId, Api5CtlCls.SW_ON)
    else: http_api_1_5(sId, Api5CtlCls.SW_OFF)