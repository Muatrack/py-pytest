import pytest
import websockets as ws
# import pytest_asyncio as asyncio
import asyncio

@pytest.mark.asyncio
async def send_msg(websocket, item):
    while True:
        await websocket.send('PING')
        item.resp = await websocket.recv()
        print(f"{item.resp}")
        break

# 客户端主逻辑
@pytest.mark.asyncio
async def ws_perform(item):
    async with ws.connect(item.uri) as c:
        await send_msg(c, item)

@pytest.fixture(scope='module')
def pytest_yaml_run_step(item):
    step = item.current_step
    request = step.get('request')
    response = step.get('response')

    if request:
        print(f'uri={request["uri"]}')
        item.uri=request["uri"]
        asyncio.run( ws_perform(item) )

    if response:
        print("got responses :\n", item.resp)
        # responses_validator.validator(item.resp, **response)
        # responses_validator.validator(item.resp, status_code=200, text='*ws_state*')

    return True

