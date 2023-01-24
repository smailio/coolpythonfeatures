import requests
from concurrent.futures import ThreadPoolExecutor
from functools import wraps
from time import time

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

def make_request(*args):
    url = f"https://randomuser.me/api?format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error" : True}

@timing
def make_1000_requests():
    results = []
    for i in range(1000):
        results += make_request(i)
    return results