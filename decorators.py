def cache(foo):
    _cache = {}
    def foo_wrapper(*args):
        t_args = tuple(*args)
        if t_args not in _cache:
            _cache[t_args] = foo(*args)
        return _cache[t_args]
    return foo_wrapper


def register_function():
    pass

def observable():
    pass
def log_with():
    pass
def inject():
    pass