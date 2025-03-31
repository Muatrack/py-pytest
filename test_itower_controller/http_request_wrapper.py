import requests

def http_post(url:str, json=None, data=None, timeout=3, retry:int=3):
    try:
        requests.post(url,json=json, data=data, timeout=timeout)
    except Exception as e:
        for i in range(2):
            requests.post(url,json=json, data=data, timeout=timeout)


def http_get(url:str, json=None, data=None, timeout=3, retry:int=3):
    try:
        requests.get(url,json=json, data=data, timeout=timeout)
    except Exception as e:
        for i in range(2):
            requests.get(url,json=json, data=data, timeout=timeout)