import asyncio
from bleak import BleakScanner

async def search_devices():
    print("Searching for nearby Bluetooth devices...")
    devices = await BleakScanner.discover()
    
    if not devices:
        print("No Bluetooth devices found nearby.")
        return
    
    print("Found {} devices nearby:".format(len(devices)))
    for device in devices:
        print("  - {} ({})".format(device.name, device.address))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(search_devices())
