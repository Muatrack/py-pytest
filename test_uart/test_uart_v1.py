import pytest
# import ../components/uart/uart.py

@pytest.fixture
def run_fixture():
    print("Before testing")

    yield

    print("After testing")

@pytest.mark.uart
# @pytest.fixture("run_fixture")
def test_uart_write(run_fixture):
# def test_uart_write():
    print("I am pstest tcase, uart modules")
