import random

import pytest

from solutions import (
    flat_list,
    create_intervals,
    inc_all,
    inifite_rand_int,
    chain,
    iterate,
    sliding_window,
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
    assert list(chain([1, 2, 3], [4, 5, 9])) == [1, 2, 3, 4, 5, 9]
    assert list(chain([], [4, 5, 9])) == [4, 5, 9]
    assert list(chain([1, 2, 3], [])) == [1, 2, 3]


def test_iterate():
    number_of_iteration = random.randint(0, 100)
    prev = 0
    int_stream = iterate(lambda x: x + 1, prev)
    for _ in range(number_of_iteration):
        n = next(int_stream)
        assert prev + 1 == n
        prev = n

    number_of_iteration = random.randint(0, 100)
    prev = 1
    power_of_2_stream = iterate(lambda x: x * 2, prev)
    for _ in range(number_of_iteration):
        n = next(power_of_2_stream)
        assert prev * 2 == n
        prev = n


def test_slicing_window():
    assert list(sliding_window(2, [1, 2, 3, 4])) == [(1, 2), (2, 3), (3, 4)]
    assert list(sliding_window(2, [9, 8, 12])) == [(9, 8), (8, 12)]
    assert list(sliding_window(2, [])) == []
    assert list(sliding_window(3, [1, 2, 3, 4])) == [(1, 2, 3), (2, 3, 4)]
    assert list(sliding_window(3, [9, 8, 12])) == [(9, 8, 12)]
    assert list(sliding_window(3, [9, 8])) == [(9, 8)]
    assert list(sliding_window(3, [])) == []
    assert list(sliding_window(1, [1, 2, 3, 4])) == [(1,), (2,), (3,), (4,)]
    assert list(sliding_window(1, [9, 8, 12])) == [(9,), (8,), (12,)]
    assert list(sliding_window(1, [])) == []


@pytest.mark.parametrize(
    "expected_results",
    [
        random.randint(0, 100),
        random.randint(0, 100),
        random.randint(0, 100),
        random.randint(0, 100),
        random.randint(0, 100),
        random.randint(0, 100),
    ],
)
def test_random_generator(expected_results):
    call_to_producer = 0

    def get_rand_int():
        nonlocal call_to_producer
        call_to_producer += 1
        return random.randint(0, 100)

    for i, e in enumerate(inifite_rand_int(get_rand_int)):
        if e == expected_results:
            assert (i + 1) == call_to_producer
            break


def test_apply_function_to_a_huge_collection():
    l = ([0] * 10000000 for _ in range(0, 1000))
    l = inc_all(l)
    l_len = 0
    expected_elem = [1] * 10000000
    for actual_elem in l:
        l_len += 1
        assert actual_elem == expected_elem
    assert l_len == 1000


def sum_all(l):
    for e in l:
        yield sum(e)


def test_create_intervals():
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)]
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)]




def double_number():
    print("0")
    number = yield
    print("1")
    while True:
        number *= 2
        print("2")
        number = yield number

if __name__ == '__main__':
    # gen = double_number()
    # print("start")
    # print(gen.send(None))
    # print("send 7")
    # print(gen.send(7))
    # print("send 11")
    # print(gen.send(11))
    # print(gen.send(13))

    it = flat_list([1, [2, 2, 3], 4, 5])
    for e in it:
        print(e)
        if e == 3:
            break
    print("salut")
    for e in it:
        print(e)
