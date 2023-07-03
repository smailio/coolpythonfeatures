import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from generate_user_name import make_request, make_1000_requests, timing

@timing
def make_1000_requests_with_threadpool():
    # ThreadPoolExecutor , make_request, submit / map 
    futures = []
    with ThreadPoolExecutor(max_workers=40) as executor:
        for i in range(1000):
            futures += [executor.submit(make_request, i)]
    results = [f.result() for f in futures]
    print(len(futures))
    
@timing
def make_1000_requests_with_processpool():
    futures = []
    with ProcessPoolExecutor(max_workers=8) as executor:
        for i in range(1000):
            futures += [executor.submit(make_request, i)]
    results = [f.result() for f in futures]
    print(len(results))

@timing
def make_1000_requests_with_asyncio():
    pass         


if __name__ == '__main__':
    make_1000_requests_with_threadpool()
    make_1000_requests_with_processpool()
    # make_1000_requests_with_asyncio()
