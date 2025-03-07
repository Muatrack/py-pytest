import pytest
from components.uart import uart

performCounter = 0

@pytest.fixture(scope="module")
def uart_handle():
    global performCounter
    performCounter += 1
    print("\n uart_handle run times:", performCounter)
    handle = uart.UART('/dev/ttyUSB0', 115200)
    handle.open()
    return handle

@pytest.fixture(scope="module")
@pytest.mark.usefixtures('uart_handle')
def uart_close(uart_handle):
    yield
    print("\n uart_handle gonna close")
    uart_handle.close()


@pytest.mark.usefixtures('uart_handle')
@pytest.mark.uart_api_elcgw
def test_uart_write(uart_handle):
    global performCounter
    print("\nI am pstest tcase, uart modules: test_uart_write(), fixture counter:", performCounter)
    uart_handle.write(b'0x9029888399232')

@pytest.mark.usefixtures('uart_handle')
@pytest.mark.uart_api_elcgw
def test_uart_read(uart_handle):
    global performCounter
    print("\nI am pstest tcase, uart modules: test_uart_read(), fixture counter:", performCounter)


@pytest.mark.uart_api_elcgw
@pytest.mark.usefixtures('uart_close')
def test_uart_close(uart_close):
    pass
