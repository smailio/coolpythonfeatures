import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from generate_user_name import make_request, make_1000_requests, timing

@timing
def make_1000_requests_with_threadpool():
    results = []
    with ThreadPoolExecutor(max_workers=64) as executor:
        results = list(executor.map(make_request, range(1000)))
    print(len(results))

@timing
def make_1000_requests_with_processpool():
    with ProcessPoolExecutor(max_workers=32) as executor:
        results = list(executor.map(make_request, range(1000)))
    print(len(results))


async def make_1000_requests_with_asyncio():
    async def make_request_async():
        # return await asyncio.get_running_loop().run_in_executor(None, make_request, 1)
        return make_request(0)
    
        # tasks = [make_request_async() for _ in range(1000)]
    tasks = [asyncio.create_task(make_request_async()) for _ in range(120)]
    results = await asyncio.gather(*tasks)
    print(len(results))
        

        


if __name__ == '__main__':
    make_1000_requests()
    # make_1000_requests_with_threadpool()
    # make_1000_requests_with_processpool()
    # make_1000_requests_with_asyncio()
    asyncio.run(make_1000_requests_with_asyncio())
