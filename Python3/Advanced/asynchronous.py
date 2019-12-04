import asyncio
import time

async def count():
    asyncio.sleep(1)
    print("OMG I am Asynchronous")
    asyncio.sleep(2)
    print("OMG I am Asynchronous call again")
    
    return 
    
    
async def sum_values():
    asyncio.sleep(3)
    print("I am counting data")
    r = count()
    print("I am back here")
    return r


loop = asyncio.get_event_loop()
loop.run_until_complete(sum_values())
loop.close()

