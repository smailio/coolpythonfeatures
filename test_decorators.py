from decorators import cache, register_function,  observable, log_with, inject


def test_cache():
    foo_count_call = [0]

    @cache
    def foo(name):
        foo_count_call[0] += 1
        return f'hello {name}'

    assert foo("jean") == 'hello jean'
    assert foo("jean") == 'hello jean'
    assert foo_count_call[0] == 1


def test_log_with():

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
        pass

    @register_function(my_functions)
    def foo2():
        pass

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