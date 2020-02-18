import sqlite3
from descriptor.descriptors import myclassmethod, mystaticmethod, normal_method, myproperty, mycachedproperty, Account


def test_static_classic_method():
    class A:

        some_attribute = "some_value"

        def __init__(self, name):
            self.name = name

        def foo(self):
            return self.name

        @mystaticmethod
        def static_foo(o):
            return o.name

        @myclassmethod
        def class_foo(cls):
            return cls.some_attribute

    a = A("jean")
    assert a.foo() == "jean"
    assert a.static_foo(A("mouloud")) == "mouloud"
    assert a.class_foo() == "some_value"

    def get_name(self):
        return self.name

    assert get_name(a) == "jean"

    A.get_name = get_name

    assert a.get_name() == "jean"

    def some_function():
        return "doing some stuff"

    A.some_function = mystaticmethod(some_function)

    assert a.some_function() == "doing some stuff"

    def get_name_upper(self):
        return self.name.upper()

    A.get_name_upper = normal_method(get_name_upper)

    assert a.get_name_upper() == "JEAN"


def test_property():

    heavy_p_call_count = [0]
    class A:

        @myproperty
        def p(self):
            return "some property"

        @mycachedproperty
        def heavy_p(self):
            heavy_p_call_count[0] += 1
            return "this took a lot of compute power"

    a = A()
    assert heavy_p_call_count[0] == 0
    assert a.p == "some property"
    assert a.heavy_p == "this took a lot of compute power"
    assert a.heavy_p == "this took a lot of compute power"
    assert heavy_p_call_count[0] == 1


def test_account():
    conn = sqlite3.connect('test_magic_methods_db.db')
    c = conn.cursor()
    c.execute('DELETE FROM accounts')
    conn.commit()
    account = Account('1')
    account.balance = 20
    account2 = Account(1)
    assert account2.balance == 20
    c.execute('select * from accounts')
    row = c.fetchone()
    c.close()
    assert row[0] == '1' and row[1] == 20

