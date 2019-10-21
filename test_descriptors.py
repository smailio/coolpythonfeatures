import sqlite3
from descriptors import (
    myclassmethod,
    mystaticmethod,
    normal_method,
    myproperty,
    mycachedproperty,
    Account,
)


def test_static_classic_method():
    """
    For this test you'll need to implement your own classmethod and
    staticmethod decorators.
    """

    class A:

        some_attribute = "some_value"

        def __init__(self, name):
            self.name = name

        def foo(self):
            return self.name

        @mystaticmethod
        def static_foo(o):
            """
            static_foo doesn't receive the instance as a first argument.
            """
            return o.name

        @myclassmethod
        def class_foo(cls):
            """
            class_foo doesn't receive the instance as first argument but the
            type of the instance.
            :return:
            """
            return cls.some_attribute

    a = A("jean")
    assert a.foo() == "jean"
    assert a.static_foo(A("mouloud")) == "mouloud"
    assert a.class_foo() == "some_value"

    """
    Here we create a simple function get_name, then we attach this function to 
    the class, it becomes a bound method, python does this behind the scenes 
    so you don't need to worry about wrapping into a descriptor to handle 
    passing the instance as a first argument.
    """

    def get_name(self):
        return self.name

    assert get_name(a) == "jean"

    A.get_name = get_name

    assert a.get_name() == "jean"

    """
    We do the same thing with some_function, except that we use 
    mystaticmethod tp wrap it into a descriptor so that some_function becomes 
    a static method.
    """

    def some_function():
        return "doing some stuff"

    A.some_function = mystaticmethod(some_function)

    assert a.some_function() == "doing some stuff"

    """
    Even if python automatically transform a function into a method when 
    you add the function to the class, I suggest writing implementing your 
    own version in normal_method.  
    """

    def get_name_upper(self):
        return self.name.upper()

    A.get_name_upper = normal_method(get_name_upper)

    assert a.get_name_upper() == "JEAN"


def test_property():
    """
    Here you'll need to implement your own version ot the property decorator,
    it will turn a method into a descriptor object, that will evaluate to
    return value of the function.

    Also the mycachedproperty that call the function only the first time
    it is called and then store the return value somewhere and will evaluate
    to it.
    """
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
    """
    Here you'll need to create the class Account.
    This class has 2 fields id and balance.
    When you create an instance of account with a new id, a row will be inserted
    in the accounts table in sqllite3 in test_descriptors_db.db.
    When you create an instance of account with an existing id it will read the
    row from the database and initialize the instance with it.
    When you update and instance of account, an update will be performed on the
    database for the related row.
    """
    conn = sqlite3.connect("test_descriptors_db.db")
    c = conn.cursor()
    c.execute("DELETE FROM accounts")
    conn.commit()
    account = Account("1")
    account.balance = 20
    account2 = Account(1)
    assert account2.balance == 20
    c.execute("select * from accounts")
    row = c.fetchone()
    c.close()
    assert row[0] == "1" and row[1] == 20
