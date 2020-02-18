from tricks.tricks import (create_zigzag, panagram, reverse_string,
                           remove_duplicates, transpose, anagrams, find_secret,
                           merge_dicts, non_unique_elements, most_frequent_elements,
                           is_ascending, sum_even_mult_last, friendly_number, find_path)


def test_reverse_string():
    assert reverse_string("abcde") == "edcba"
    assert reverse_string("aaa") == "aaa"
    assert reverse_string("aaaeee") == "eeeaaa"
    assert reverse_string("a") == "a"
    assert reverse_string("") == ""


def test_anagram():
    assert anagrams("Programming", "Gram Ring Mop")
    assert not anagrams("Hello", "Ole Oh")
    assert anagrams("Kyoto", "Tokyo")


def test_remove_duplicates():
    from collections import Counter
    assert Counter(remove_duplicates([1, 2, 3])) == Counter([1, 2, 3])
    assert Counter(remove_duplicates([1, 2, 2, 3])) == Counter([1, 2, 3])
    assert Counter(remove_duplicates([2, 2])) == Counter([2])
    assert Counter(remove_duplicates([2])) == Counter([2])
    assert remove_duplicates([]) == []


def test_non_unique_elements():
    assert non_unique_elements([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
    assert non_unique_elements([1, 2, 3, 4, 5]) == []
    assert non_unique_elements([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    assert non_unique_elements([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]


def test_most_frequent_element():
    assert most_frequent_elements([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'
    assert most_frequent_elements(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'


def test_transpose():
    assert transpose([[1, 2], ['a', 'b']]) == [(1, 'a'), (2, 'b')]
    assert transpose([[1, 2, 3], ['a', 'b', 'c']]) == [(1, 'a'), (2, 'b'), (3, 'c')]


def test_panagram():
    assert panagram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not panagram("ABCDEF"), "ABC"
    assert panagram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"


def test_find_secret():
    assert find_secret("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
    assert find_secret("hello world!") == ""


def test_merge_dicts():
    assert merge_dicts({"a": "anis"}, {"b": "bernard"}) == {"a": "anis", "b": "bernard"}
    assert merge_dicts({"b": "bilal"}, {"b": "bernard"}) == {"b": "bernard"}
    assert merge_dicts({}, {"b": "bernard"}) == {"b": "bernard"}
    assert merge_dicts({"a": "anis"}, {}) == {"a": "anis"}
    assert merge_dicts({}, {}) == {}


def test_is_ascending():
    assert is_ascending([-20, -5, 10, 15])
    assert not is_ascending([-20, -5, 20, 15])
    assert not is_ascending([1, 2, 3, 0])
    assert not is_ascending([-1, -2, -3, 0])
    assert is_ascending([1, 2, 3])


def test_create_zigzag():
    # These "asserts" are used for self-checking and not for an auto-testing
    assert create_zigzag(3, 5) == [
        [1, 2, 3, 4, 5],
        [10, 9, 8, 7, 6],
        [11, 12, 13, 14, 15]
    ]
    assert create_zigzag(5, 1) == [
        [1],
        [2],
        [3],
        [4],
        [5]
    ]
    assert create_zigzag(3, 3, 5) == [
        [5, 6, 7],
        [10, 9, 8],
        [11, 12, 13]
    ]

    # Edge cases
    assert create_zigzag(0, 3) == []
    assert create_zigzag(3, 0) == [[], [], []]
    assert create_zigzag(0, 0) == []


def test_sum_even_mult_last():
    assert sum_even_mult_last([0, 1, 2, 3, 4, 5]) == 30
    assert sum_even_mult_last([1, 3, 5]) == 30
    assert sum_even_mult_last([6]) == 36
    assert sum_even_mult_last([]) == 0


def test_friendly_number():
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'


def test_find_path():
    def check_route(func, labyrinth):
        MOVE = {"S": (1, 0), "N": (-1, 0), "W": (0, -1), "E": (0, 1)}
        #copy maze
        route = func([row[:] for row in labyrinth])
        pos = (1, 1)
        goal = (10, 10)
        for i, d in enumerate(route):
            move = MOVE.get(d, None)
            if not move:
                print("Wrong symbol in route")
                return False
            pos = pos[0] + move[0], pos[1] + move[1]
            if pos == goal:
                return True
            if labyrinth[pos[0]][pos[1]] == 1:
                print("Player in the pit")
                return False
        print("Player did not reach exit")
        return False

    # These assert are using only for self-testing as examples.
    assert check_route(find_path, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "First maze"
    assert check_route(find_path, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Empty maze"
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Up and down maze"
    assert check_route(find_path, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Dotted maze"
    assert check_route(find_path, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Need left maze"
    assert check_route(find_path, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "The big dead end."