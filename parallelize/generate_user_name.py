import requests
from concurrent.futures import ThreadPoolExecutor
from functools import wraps
from time import time
import aiohttp


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        elapsed = te-ts
        print(f"func {f.__name__} took: {elapsed} sec")
        return result
    return wrap

def atiming():
    def wrapper(f):
        @wraps(f)
        async def wrap(*args, **kw):
            ts = time()
            result = await f(*args, **kw)
            te = time()
            elapsed = te-ts
            print(f"func {f.__name__} took: {elapsed} sec")
            return result
        return wrap
    return wrapper

def make_request(*args):
    url = f"https://randomuser.me/api?format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error" : True}

async def make_request_with_aiohttp():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://randomuser.me/api?format=json') as response:
            r = response.text()
            return await r

def intense_work(n):
    a = n
    for i in range(1, 30000):
        a = a * i
    return a

@timing
def make_1000_requests():
    results = []
    for i in range(20):
        for j in range(50): 
            results += make_request(i)
    return results