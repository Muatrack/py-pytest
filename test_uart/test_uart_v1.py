import pytest
# import ../components/uart/uart.py

@pytest.mark.usefixtures('env_fixture_package')
@pytest.mark.usefixtures('uart_fixture_module')
@pytest.mark.uart
def test_uart_write():
    print("I am pstest tcase, uart modules: test_uart_write()")

@pytest.mark.usefixtures('env_fixture_package')
@pytest.mark.usefixtures('uart_fixture_module')
@pytest.mark.uart
def test_uart_read():
    print("I am pstest tcase, uart modules: test_uart_read()")
