from typing import Iterable, List
import itertools
import operator


def reverse_string(s):
    return s[::-1]


def anagrams(s1, s2):
    from collections import Counter
    return Counter(s1.lower().replace(' ', '')) == Counter(s2.lower().replace(' ', ''))


def non_unique_elements(data):
    return [i for i in data if data.count(i) > 1]


def most_frequent_elements(l):
    return max(set(l), key=l.count)


def transpose(l):
    return list(zip(*l))


def merge_dicts(d1, d2):
    return {**d1, **d2}


def remove_duplicates(l):
    return list({e for e in l})

"""
def panagram(text):
    return set(ascii_lowercase).issubset(set(text.lower()))
"""


def panagram(text):
    from string import ascii_lowercase
    return set(ascii_lowercase).issubset(set(text.lower()))


def sum_even_mult_last(array):
    return sum(el for el in array[::2]) * array[-1] if array else 0


def find_secret(text):
    return ''.join(filter(str.isupper, text))


# def create_zigzag(rows: int, cols: int, start: int = 1) -> List[List[int]]:
#     return [
#         [start + col + cols * row for col in (range(cols) if not row % 2 else reversed(range(cols)))]
#         for row in range(rows)
#     ]


# def create_zigzag(rows: int, cols: int, start: int = 1) -> List[List[int]]:
#     from itertools import count, islice
#     it = count(start)
#     return [list(islice(it, cols))[::(-1) ** row] for row in range(rows)]


def create_zigzag(r: int, c: int, s: int = 1) -> List[List[int]]:
    return [sorted(range(s + c * i, s + c * (i + 1)), reverse=bool(i % 2)) for i in range(r)]


# def is_ascending(items: List[int]) -> bool:
#     return len(items) < 2 or all(item < next_item for item, next_item in zip(items[:-1], items[1:]))


# def is_ascending(items: Iterable[int]) -> bool:
#     return all(items[i] < items[i+1] for i in range(len(items)-1))


# def is_ascending(items: Iterable[int]) -> bool:
#     items, shifted = itertools.tee(items)
#     next(shifted, None)
#     return all(map(operator.lt, items, shifted))


def is_ascending(x):
    return sorted(set(x)) == x


def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    # At first, decompose the number to value and exponent.
    e = 0
    while e + 1 < len(powers) and abs(number) >= base ** (e + 1) : e += 1
    number /= base ** e
    # Then round it.
    number = round(number, decimals) if decimals else int(number)
    # At last, Format it.
    return '{:.0f}'.replace('0', str(decimals)).format(number) + powers[e] + suffix


def find_path(data):
    def explore(path, i, j):
        """Yields all possible solutions starting with path, from (i,j)."""
        if i == j == 10:
            yield path  # found a solution
        if not data[i][j]:  # free way
            data[i][j] = 2  # block already traversed path to prevent loops
            for i, j, way in (i-1,j,'N'), (i+1,j,'S'), (i,j-1,'W'), (i,j+1,'E'):
                yield from explore(path + way, i, j)  # explore all four ways
    return next(explore('', 1, 1))
