def cache(fun):
    _cache = {}

    def _fun(*args):
        if args not in _cache:
            _cache[args] = fun(*args)
        return _cache[args]

    return _fun


def register_function(l):
    def dec(fun):
        l.append(fun)
        return fun
    return dec


def observable(l):
    observers = []

    def observer(fun):
        observers.append(fun)
        return fun

    def append(e):
        l.append(e)
        for observer in observers:
            observer(e)

    def get_value():
        from copy import deepcopy
        return deepcopy(l)

    return append, observer, get_value


def log_with(logger):
    def dec(fun):
        def _fun(*args):
            fun_call_log = f"{fun.__name__}({', '.join(str(arg) for arg in args)})"
            logger(f"call {fun_call_log}")
            ret = fun(*args)
            logger(f"{fun_call_log} returns {ret}")
            return ret
        return _fun
    return dec


def inject(**kwargs):
    def dec(fun):
        def decorated_fun(*args, **kwargs2):
            return fun(*args, **kwargs, **kwargs2)
        return decorated_fun
    return dec
