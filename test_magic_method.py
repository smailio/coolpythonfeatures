from magic_methods import select, table


def test_select_from():
    class Customer:
        name = "string"
        category = "string"

    customer = table(Customer)
    q = select(customer.name).frm(customer)
    assert str(q) == "select customer.name from customer"


def test_select_from_where():
    class Customer:
        name = "string"
        category = "string"

    customer = table(Customer)
    category_is_gold = customer.category == "gold"
    q = select(customer.name).frm(customer).where(category_is_gold)
    assert (
        str(q) == "select customer.name from customer where customer.category = 'gold'"
    )


def test_select_from_where2():
    class Customer:
        name = "string"
        category = "string"

    customer = table(Customer)
    category_is_gold = "gold" == customer.category
    q = select(customer.name).frm(customer).where(category_is_gold)
    assert (
        str(q) == "select customer.name from customer where customer.category = 'gold'"
    )


def test_select_from_where_and():
    class Customer:
        name = "string"
        category = "string"
        size = "string"

    customer = table(Customer)
    category_is_gold = customer.category == "gold"
    size_is_big = customer.size == "BIG"
    q = select(customer.name).frm(customer).where(category_is_gold & size_is_big)
    assert (
        str(q) == "select customer.name from customer "
        "where ( customer.category = 'gold' and customer.size = 'BIG' )"
    )
    q = select(customer.name).frm(customer).where(size_is_big & category_is_gold)
    assert (
        str(q) == "select customer.name from customer "
        "where ( customer.size = 'BIG' and customer.category = 'gold' )"
    )


def test_select_from_where_or():
    class Customer:
        name = "string"
        category = "string"

    customer = table(Customer)
    category_is_gold = customer.category == "gold"
    q = select(customer.name).frm(customer).where(category_is_gold)
    assert (
        str(q) == "select customer.name from customer where customer.category = 'gold'"
    )
