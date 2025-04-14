import requests

"""
    电力网关http api
"""

''' http 请求头-授权 '''
httpd_header={'ookie': 'auth_key=Basic ZXNwMzI6NjY2ODg4'}

def http_api_server_get():
    resp = requests.get('http://192.168.31.30/server', headers=httpd_header ,timeout=5)
    assert resp.status_code==200    
    # print(resp.text)
    return {}
