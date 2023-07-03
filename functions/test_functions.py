from functions.solutions import make_wrap, make_append_only_list, mymap

"""
Functions are first class citizen in Python, which means you can pass them to other functions as arguments, 
return them from other functions as values, and store them in variables and data structures

python -m venv .venv
source .venv/bin/activate
python -m pip install pytest
"""


def test_wrapper():
    """
    Here you'll need to implement a make_wrap function, this function take
    one or two strings and returns a ... function !
    Because in Python a function can return a function. So if you do this :
    > quote = make_wrap("'")
    quote is a function and you can call it like this :
    > quote("hello")
    ... 'hello'
    You see quote returned hello wrapped in a single quote.
    """
    quote = make_wrap("'")
    comment = make_wrap('/*', '*/')
    wrap_with_div = make_wrap("<div>", "</div>")

    assert quote("salut") == "'salut'"
    assert make_wrap('"')("salut") == '"salut"'
    assert comment("salut") == '/*salut*/'
    assert wrap_with_div("salut") == '<div>salut</div>'


def test_make_append_only_list():
    """
    Here you'll need to implement make_append_only_list, which is
    also a function that returns a function, actually 2 functions.
    The first function that make_append_only_list returns : you can use
    it to add element to a list, a list to which you don't have access.
    The second function you can use it to get a copy of the list.
    """
    append, get_l1 = make_append_only_list()
    append({"name": "jean"})
    append({"name": "mohammed"})
    l_copy = get_l1()
    assert l_copy == [{"name": "jean"}, {"name": "mohammed"}]
    append({"name": "mouloud"})
    assert l_copy == [{"name": "jean"}, {"name": "mohammed"}]
    l_copy = get_l1()
    assert l_copy == [{"name": "jean"}, {"name": "mohammed"}, {"name": "mouloud"}]
    l_copy.append({"name": "edouard"})
    assert [{"name": "jean"}, {"name": "mohammed"}, {"name": "mouloud"}] == get_l1()

def test_mymap():
    assert mymap(["a", "b"], str.upper) == ["A", "B"]
    assert mymap(["a", "b"], make_wrap("(", ")")) == ["(a)", "(b)"]
