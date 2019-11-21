import random
from generators_solution import (
    flat_list,
    create_intervals,
    add_one,
    produce_untill,
    chain,
)


def test_flatten_list():
    assert list(flat_list([1, 2, 3])) == [1, 2, 3], "First"
    assert list(flat_list([1, [2, 2, 2], 4])) == [1, 2, 2, 2, 4], "Second"
    assert list(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])) == [
        2,
        4,
        5,
        6,
        6,
        6,
        6,
        6,
        7,
    ], "Third"


def test_chain():
    assert chain([1, 2, 3], [4, 5, 9]) == [1, 2, 3, 4, 5, 9]
    assert chain([], [4, 5, 9]) == [4, 5, 9]
    assert chain([1, 2, 3], []) == [1, 2, 3]


def test_random_generator():
    call_to_producer = 0

    expected_results = random.randint(0, 9)

    def producer():
        nonlocal call_to_producer
        call_to_producer += 1
        return random.randint(0, 100)

    produce_untill_len = 0
    for e in produce_untill(producer, lambda x: x == expected_results):
        produce_untill_len += 1
        if e == expected_results:
            assert produce_untill_len == call_to_producer


def test_apply_function_to_a_huge_collection():
    l = range(0, 100000)
    number_of_iteration = random.randint(9, 12)
    for _ in [0] * number_of_iteration:
        l = add_one(l)
    l_len = 0
    print(list(l))
    for e in l:
        l_len += 1
        print(e)
        assert (e - 1) == number_of_iteration
    assert l_len == 1000000000
    # assert list(l) == [number_of_iteration] * 10000000


def test_create_intervals():
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)]
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)]
