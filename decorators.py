def cache(foo):

    tCacheText = {}

    def foo_wrapper(name):

        if name in tCacheText:
            return tCacheText[name]
        else:
            tCacheText[name] = foo(name)
            return tCacheText[name]

    return foo_wrapper


def register_function(my_functions):
    def foo_decorator(foo):

        my_functions.append(foo)

        return foo

    return foo_decorator


def observable(l):

    my_functions = []

    def append(value):
        l.append(value)
        for f in my_functions:
            f(value)

    return append, register_function(my_functions)


def log_with(list_logger):
    def foo_decorator(foo):
        def foo_wrapper(x, y):

            fooRes = foo(x, y)
            sFunction = str(foo.__name__) + "(" + str(x) + ", " + str(y) + ")"
            sFirstRes = "call " + sFunction
            sSecondRes = sFunction + " returns " + str(fooRes)
            list_logger(sFirstRes)
            list_logger(sSecondRes)

        return foo_wrapper

    return foo_decorator


def inject(dep):
    def foo_decorator(foo):
        def foo_wrapper(*args):
            return foo(args[0], dep)

        return foo_wrapper

    return foo_decorator
