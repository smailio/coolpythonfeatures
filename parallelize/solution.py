from generate_user_name import make_request, make_1000_requests, timing

def make_1000_requests_with_threadpool():
    make_request(0) 


def make_1000_requests_with_processpool():
    make_request(0) 


def make_1000_requests_with_asyncio():
    make_request(0) 


if __name__ == '__main__':
    make_1000_requests()