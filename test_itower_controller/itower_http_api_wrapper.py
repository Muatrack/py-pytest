from itower_http_api_lib import *
import time

def slave_mgr_list_query():
    '''
        查询设备列表

        :return 设备数量，设备列表:
    '''

    resp = http_api_1_1()
    assert resp.status_code==200
    body = resp.json()
    assert body['code']==1000    
    originList:list = body['data']['list']
    originCount:int = body['data']['count']
    return originCount, originList

def slave_mgr_data_query(sId:int):
    http_api_1_2()

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