"""Example for Climate device."""
import asyncio

import sys


#import xknx
from xknx import XKNX
from xknx.devices import Climate



async def main():
    """Connect to KNX/IP and read the state of a Climate device."""
    xknx = XKNX()
    async with xknx:
        climate = Climate(xknx, "Büro", group_address_temperature="1/4/121")
        await climate.sync(wait_for_result=True)
        # Will print out state of climate including current temperature:
        print(climate.temperature)


asyncio.run(main())

