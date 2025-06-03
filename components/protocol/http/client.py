import requests
from  .interface import ClientIF

class Client(ClientIF):
    
    def __init__(self):
        pass

    def Get(self, url:str):
        '''
            发送get请求
        '''
        resp = requests.get(url)
        return resp
    
    def Post(self, url:str, headers:dict=0, payload:dict=0):
        '''
            发送post请求
        '''
        resp = requests.get(url)
        return resp