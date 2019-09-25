def make_wrap(c, c2=None):
    if c2 is None:
        c2 = c

    def wrap(s):
        return c + s + c2

    return wrap


def make_append_only_list():
    append_only_list = []

    def append(e):
        append_only_list.append(e)

    def copy():
        from copy import deepcopy
        return deepcopy(append_only_list)

    return append, copy


def mymap(l, f):
    return [f(e) for e in l]
