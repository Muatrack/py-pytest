import pytest
import time

@pytest.mark.perform_order
class TestDemo:

    # @pytest.mark.perform_order
    def test_perform_o1(self):
        print("perform_o1 .")
        time.sleep(0.2)

    # @pytest.mark.perform_order
    def test_perform_o2(self):
        print("perform_o2 .")
        time.sleep(0.2)


