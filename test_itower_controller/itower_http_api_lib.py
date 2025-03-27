import requests
from enum import Enum

baseUrl='http://192.168.20.1'
httpd_header={'ookie': 'auth_key=Basic ZXNwMzI6NjY2ODg4'}

class Api5CtlCls(Enum):
    SW_ON   =   0
    SW_OFF  =   1
    AIR_ON  =   2
    AIR_OFF =   3

def http_api_1_1():
    """
    查询设备列表
    """
    resp = requests.get(baseUrl+'/v1/api/slave', timeout=3)
    assert resp.status_code==200
    return resp

def http_api_1_2():
    """ 
    查询子设备(id)采集数据
    e.g. 温度传感器的温度，采集器的电流、电压 ...
    """
    resp = requests.get(baseUrl+'/v1/api/slave?id=1', timeout=3)
    assert resp.status_code==200
    return resp

def http_api_1_3():
    """ 
    增加子设备
    """
    data={
        "action": "new",
        "params": {
            "name": "5Lit5paH57yW56CB5aW95aOw6Z+z5aSn5biI6K6+",
            "parentId": 0,
            "sn": "170902FB2340E011",
            "exta":{
                "tempApplyEnv":0
            }
        }
    }
    resp = requests.post(baseUrl+'/v1/api/slave?id=1',data=data, timeout=3)
    assert resp.status_code==200
    return resp

def http_api_1_4():
    """ 
    删除子设备
    """
    data={
    }
    resp = requests.post(baseUrl+'/v1/api/slave?id=1',data=data, timeout=3)
    assert resp.status_code==200
    return resp

def http_api_1_5(sId:int, ctlCls:Api5CtlCls):
    """ 
    控制子设备(仅采集器)  e.g. 分/合闸，开/关机

        :param sId: 子设备ID [1-31]
        :param ctlCls: 控制分类 [开机、关机、合闸、分闸]

    """
    data={
        "action": "ctrl",
        "params": {
            "id": 30,       #设备ID
            "ctrlType": 1,  # 1:分合闸, 2:开关机
            "ctrlValue": 1, # 0:关闭，  1:打开
            "aircMode": 0,  # def:0
            "aircTemp": 0   # def:23
        }
    }

    if ctlCls==Api5CtlCls.SW_OFF:
        data["params"]["ctrlType"]=1
        data["params"]["ctrlValue"]=0

    if ctlCls==Api5CtlCls.SW_ON:
        data["params"]["ctrlType"]=1
        data["params"]["ctrlValue"]=1

    if ctlCls==Api5CtlCls.AIR_OFF:
        data["params"]["ctrlType"]=2
        data["params"]["ctrlValue"]=0

    if ctlCls==Api5CtlCls.AIR_ON:
        data["params"]["ctrlType"]=2
        data["params"]["ctrlValue"]=1

    resp = requests.post(baseUrl+'/v1/api/slave?id=1',data=data, timeout=3)
    assert resp.status_code==200
    return resp

def http_api_1_6(sId:int, attributes:object):
    """
    修改子设备的属性，可修改的属性有名称、父设备id

    :param sId 子设备的id
    :param attributes 修改后的属性对象
        {
            "name": base64编码名称，
            "pid": 父设备id
        }        
    """

    data={
            "action": "mod", # 固定
            "params": {
                "id": 2,    #设备id
                "exta": {   #温度传感器的预设安装位置ID
                    "tempApplyEnv": 0
                }
            }
        }
    
    if attributes["name"]:
        data["name"]=attributes["name"]
    if attributes["pid"]:
        data["pid"]=attributes["pid"]

    resp = requests.post(baseUrl+'/v1/api/slave',data=data, timeout=3)
    assert resp.status_code==200
    return resp

def http_api_2_2(sId:int, attributes:object):
    """
    重启系统
    """
    resp = requests.post(baseUrl+'/v1/api/slave',data=data, timeout=3)
    assert resp.status_code==200
    return resp

def http_api_2_3(sId:int, attributes:object):
    """
    提交授权码
    """
    data={}
    resp = requests.post(baseUrl+'/v1/api/system',data=data, timeout=3)
    assert resp.status_code==200
    return resp

def http_api_2_4(sId:int, attributes:object):
    """
    查询授权码
    """
    resp = requests.get(baseUrl+'/v1/api/system?part=aucode',timeout=3)
    assert resp.status_code==200
    return resp

def http_api_2_5(sId:int, attributes:object):
    """
    查询序列号(SN)
    """
    resp = requests.get(baseUrl+'/v1/api/system?part=sncode',timeout=3)
    assert resp.status_code==200
    return resp

def http_api_2_7(sId:int, attributes:object):
    """
    查询控制器OTA缓存
    """
    resp = requests.get(baseUrl+'/v1/api/system?part=otalist',timeout=3)
    assert resp.status_code==200
    return resp

def http_api_2_8(sId:int, attributes:object):
    """
    查询固件版本
    """
    resp = requests.get(baseUrl+'/v1/api/system?part=fwver',timeout=3)
    assert resp.status_code==200
    return resp

def http_api_2_10(sId:int, attributes:object):
    """
    查询LUA文件列表
    """
    resp = requests.get(baseUrl+'/v1/api/system?part=lualist',timeout=3)
    assert resp.status_code==200
    return resp

def http_api_2_11(sId:int, attributes:object):
    """
    查询空调配置
    """
    resp = requests.get(baseUrl+'/v1/api/system?part=airconf',timeout=3)
    assert resp.status_code==200
    return resp

def http_api_2_12(sId:int, attributes:object):
    """
    查询控制器配置
    """
    resp = requests.get(baseUrl+'/v1/api/system?part=ctlerst',timeout=3)
    assert resp.status_code==200
    return resp

def http_api_2_13(sId:int, attributes:object):
    """
    查询LTE状态
    """
    resp = requests.get(baseUrl+'/v1/api/system?part=ltestate',timeout=3)
    assert resp.status_code==200
    return resp

def http_api_2_14(sId:int, attributes:object):
    """
    查询平台地址
    """
    resp = requests.get(baseUrl+'/v1/api/system?part=platform',timeout=3)
    assert resp.status_code==200
    return resp

def http_api_2_15(addr:str):
    """
    设置平台地址
    """
    data={
        "action": "new",
        "params": {            
            "part": "platform"
        }
    }
    data["host"]=addr
    resp = requests.post(baseUrl+'/v1/api/system',data, timeout=3)
    assert resp.status_code==200
    return resp

def http_api_2_16(addr:str):
    """
    查询预设温度传感器安装位置
    """    
    resp = requests.get(baseUrl+'/v1/api/system?part=slvTempAppId',timeout=3)
    assert resp.status_code==200
    return resp

def http_api_2_17():
    """
    查询控制器已存json文件列表
    """    
    resp = requests.get(baseUrl+'/v1/api/system?part=jsonlist',timeout=3)
    assert resp.status_code==200
    return resp

def http_api_2_18():
    """
    查询控制器新/旧固件版本号及新版本应用状态
    """    
    resp = requests.get(baseUrl+'/v1/api/ota/part=all',timeout=3)
    assert resp.status_code==200
    return resp

def http_api_2_19():
    """
    应用新版本
    """    
    data={}
    resp = requests.post(baseUrl+'/v1/api/otaconfirm',data,timeout=3)
    assert resp.status_code==200
    return resp

def http_api_2_20(filepath:str):
    """
    上传控制器升级文件到到控制器
    """    
    data={}
    resp = requests.post(baseUrl+'/v1/api/ota',data,timeout=3)
    assert resp.status_code==200
    return resp
