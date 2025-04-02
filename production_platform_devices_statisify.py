import requests
import time

"""
    生产平台设备状态统计
"""

class DevicesCls:
    
    def allDevsGets(self):
        url='http://sga1.conserway.com:6011/device-service/w/device/findMasterPage?queryType=1&curPage=1&pageSize=24&keywordType=1&keyword=&modelId=&registerBeginTime=&registerEndTime=&stationId=&onlineStatus=&energySavingStatus=&runStatus=1&province=&city=&county=&_t=1743600459'
        token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM2ODY3Nzl9.qBLmI28xJyRbSRkp_PkAn6EIP7XIVpwXc1ukcsNmZCo'
        resp = requests.get(url, headers={ 'Token':token}, timeout=5)
        if resp.status_code!=200:
            print("Fail to req Get all devices")
            return
        print("Succ got devices, total: %d" % resp.json()['data']['total'])
        
if __name__ == '__main__':
    devs = DevicesCls()
    devs.allDevsGets()
    