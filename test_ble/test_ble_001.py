import pytest
from bleak import BleakScanner as bleScanner
import asyncio

# def  ble_adv_name_filter (device: BLEDevice, adv: AdvertisementData):
# 	if "AIRC-" in adv.name:
# 		return True
# 	return False

async def ble_discover():
    results = None

    print("\nble discovery Begining ...")
    results = await bleScanner.discover(timeout=10, return_adv=True)
    # results = await bleScanner.find_device_by_filter( lambda d, ad: d.name and ("AIREC-" in d.name), timeout=10 )
    if( results == None ):
        print("ble discovery result: None")
    else:
        print("\n", results)
        # for item in results:
        #     print("ble discovery result:", item, "\n")

@pytest.mark.ble_api_collector
def test_ble_discover():
    asyncio.run( ble_discover() )
