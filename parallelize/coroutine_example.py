import asyncio
from generate_user_name import timing, atiming, intense_work, make_request, make_request_with_aiohttp
import concurrent.futures


async def intense_work_async(i):
    return intense_work(i)


# @timing
# def intense_work_x_20():
#     r = 0
#     for i in range(2, 22):
#         r += intense_work(i)

# @atiming()
# async def intense_work_x_20_create_task():
#     responses = []
#     for i in range(2, 22):
#         responses+= [asyncio.create_task(intense_work_async(i))]
#     r = sum(await asyncio.gather(*responses))

# @atiming()
# async def intense_work_x_20_to_thread():
#     responses = []
#     for i in range(2, 22):
#         responses+= [asyncio.to_thread(intense_work, i)]
#     r = sum(await asyncio.gather(*responses))


@atiming()
async def intense_work_x_20_to_process():
    loop = asyncio.get_running_loop()
    responses = []
    with concurrent.futures.ProcessPoolExecutor() as pool:
        for i in range(2, 22):
            responses +=  [loop.run_in_executor(pool, intense_work, i)]
    r = sum(await asyncio.gather(*responses))

@timing
def make_120_requests():
    for _ in range(120):
        make_request(0)


@atiming()
async def make_120_requests_with_asyncio():
    async def make_request_async():
        return make_request(0)
    tasks = [asyncio.create_task(make_request_async()) for _ in range(120)]
    results = await asyncio.gather(*tasks)

@atiming()
async def make_120_requests_with_asyncio_and_aiohttp():
    tasks = [asyncio.create_task(make_request_with_aiohttp()) for _ in range(120)]
    results = await asyncio.gather(*tasks)

@atiming()
async def make_120_requests_with_asyncio_thread():
    tasks = [asyncio.to_thread(make_request, 0) for _ in range(120)]
    results = await asyncio.gather(*tasks)

async def main():    
    # intense_work_x_20()
    # await intense_work_x_20_create_task()
    # await intense_work_x_20_to_thread()
    # await intense_work_x_20_to_process()

    make_120_requests()
    await make_120_requests_with_asyncio()
    await make_120_requests_with_asyncio_thread()
    await make_120_requests_with_asyncio_and_aiohttp()

if __name__ == '__main__':
    asyncio.run(main())