def flat_list(l):
    for e in l:
        print("processing ", e)
        if isinstance(e, list):
            yield from flat_list(e)
        else:
            yield e


def create_intervals(numbers: {}) -> [()]:
    pass


def inc_all(ll: []) -> []:
    pass


def inifite_rand_int(get_rand_int):
    pass


def chain(l1, l2):
    pass


def iterate(fun, initial_value):
    pass


def sliding_window(n, seq):
    pass
