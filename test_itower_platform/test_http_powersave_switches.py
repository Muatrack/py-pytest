import pytest
import requests
# import responses_validator
import time

# 测试平台token
testToken='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM2ODQ2MDF9.I1HfFXagE7BVbJwM_6aVmANj0yuTZ-ipgB43E5ybODc'
productionToken='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM2ODY3Nzl9.qBLmI28xJyRbSRkp_PkAn6EIP7XIVpwXc1ukcsNmZCo'

# @pytest.mark.repeat(50)
@pytest.mark.http_api_platform
def test_http_api_poweroff():
    """
        节能关闭 | 空调关机 | 节能关闭
        展厅空调id: 1906954671052406785
    """

    url = 'http://116.62.168.206:6011/device-service/w/device/setAirConditionerStatus'

    headers = {
        'Token': testToken
    }

    body={
        "id": "1906954671052406785",
        "powerStatus": 2,
        "runStatus": 2,
        "energyStatus": 2
    }
    
    resp = requests.options(url, timeout=3)
    assert resp.status_code==200
    time.sleep(800)
    resp = requests.post(url, headers, json=body, timeout=3)
    assert resp.status_code==200
    time.sleep(30)


@pytest.mark.http_api_platform
def test_http_api_poweron_otheroff():
    """
        节能开启 | 空调关机 | 节能关闭
        展厅空调id: 1906954671052406785
    """
    url = 'http://116.62.168.206:6011/device-service/w/device/setAirConditionerStatus'

    headers = {
        'Token': testToken
    }
    body={
        "id": "1906954671052406785",
        "powerStatus": 1,
        "runStatus": 2,
        "energyStatus": 2
    }

    resp = requests.options(url, timeout=3)
    assert resp.status_code==200
    time.sleep(800)
    resp = requests.post(url, headers, json=body, timeout=30)
    assert resp.status_code==200
    time.sleep(30)