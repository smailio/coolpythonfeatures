from decorators.solutions import cache, register_function,  observable, log_with, inject

from typing import Callable

def test_cache():
    """
    You'll need to implement a cache function.

    The point of cache is that when you decorate a function with cache,
    then when you'll call the decorated function several times with the
    same arguments the function will run only the first time.

    The decorated function will run and save the result the first time it's called
    with a given argument, the following times it'll retrieve the result saved and return it
    without really running.

    In real life you may need a cache decorotor, the standard library provide one
    in the functools module : @functools.cached_property
    """
    foo_count_call = 0

    @cache
    def foo(name):
        nonlocal foo_count_call
        foo_count_call += 1
        return f'hello {name}'

    assert foo("jean") == 'hello jean'
    assert foo("jean") == 'hello jean'
    assert foo_count_call == 1


def test_log_with():
    """
    You'll need to implement a log_with function.

    def log_with(logger_function : Callable[[Any*], NoReturn]):
        pass
    The point of log_with is that when you decorate a function with log_with,
    then when you'll call the decorated function it'll call the logger_function

    """
    logs = []

    def list_logger(e):
        logs.append(e)

    @log_with(list_logger)
    def foo(x, y):
        return x * y

    foo(1, 2)
    foo(5, 5)

    assert logs == ["call foo(1, 2)", "foo(1, 2) returns 2", "call foo(5, 5)", "foo(5, 5) returns 25"]
    # same logic for benchmark, timeit, trace, count function call


def test_register_function():
    my_functions = []

    @register_function(my_functions)
    def foo1():
        return "hey I'm foo1"

    @register_function(my_functions)
    def foo2():
        return "hey I'm foo2"

    assert foo1() == "hey I'm foo1"
    assert foo2() == "hey I'm foo2"
    assert my_functions == [foo1, foo2]


def test_observer():
    append, observer, get_value = observable([])

    copy_of_o = []

    @observer
    def foo(e):
        copy_of_o.append(e)

    append(11)
    append(22)
    append(33)

    assert copy_of_o == [11, 22, 33]
    assert get_value() == [11, 22, 33]


def test_inject():
    @inject(dep="dependency1")
    def foo(not_dep, dep):
        return dep, not_dep

    assert foo("hello") == ("dependency1", "hello")