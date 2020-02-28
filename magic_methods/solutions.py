import re


class SelectClause:
    pass


class FromClause:
    pass


class JoinClause:
    pass


class WhereClause:
    pass


class GroupBy:
    pass


def select(*args):
    pass


def lit(value):
    pass


def lit_if_not_col(value):
    pass


class Expr:
    pass


class Column(Expr):
    pass


class EqCondition(Expr):
    pass


class AndCondition(Expr):
    pass


class OrCondition(Expr):
    pass


class Table:
    pass


class CountAgg(Expr):
    pass


def table(cls):
    pass


pattern = re.compile(r"( ){2,}")


def sql(query) -> str:
    pass


"""def distinct(col):
    return DistinctAgg(col)
"""

def count(col):
    pass
