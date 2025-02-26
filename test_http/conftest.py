import pytest
import requests
# import response

class Http:
    def connect(self):
        print("conn http conn")

    def response_cb_set(selv):
        print("set http resp cb")

    def close(self):
        print("close http conn")
    
@pytest.fixture()
def httpObj() -> object:
    return "http class object"

# @pytest.mark.usefixtures('httpObj')
@pytest.fixture(scope='module')
def http_fixture_module() -> any :
    print("\n[ Gonna open http connection ] --------------- str:", httpObj)    
    yield
    print("\n[ Close http connection ] ---------------")