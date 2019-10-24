def foo_decorator(foo):
    def foo_wrapper():
        foo()
    return foo_wrapper