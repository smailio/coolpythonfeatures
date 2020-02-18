from functions.functions import make_wrap, make_append_only_list, mymap


def test_wrapper():
    quote = make_wrap("'")
    comment = make_wrap('/*', '*/')
    wrap_with_div = make_wrap("<div>", "</div>")

    assert quote("salut") == "'salut'"
    assert make_wrap('"')("salut") == '"salut"'
    assert comment("salut") == '/*salut*/'
    assert wrap_with_div("salut") == '<div>salut</div>'


def test_make_append_only_list():
    append, get_l1 = make_append_only_list()
    append({"name": "jean"})
    append({"name": "mohammed"})
    l_copy = get_l1()
    assert l_copy == [{"name": "jean"}, {"name": "mohammed"}]
    l_copy.append({"name": "edouard"})
    assert [{"name": "jean"}, {"name": "mohammed"}] == get_l1()

def test_mymap():
    assert mymap(["a", "b"], str.upper) == ["A", "B"]
    assert mymap(["a", "b"], make_wrap("(", ")")) == ["(a)", "(b)"]
