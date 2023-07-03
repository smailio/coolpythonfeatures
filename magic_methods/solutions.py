import re


class SelectClause:
    def __init__(self, *expressions):
        self.expressions = expressions

    def frm(self, table):
        self.fromClause = FromClause(table, self)
        return self.fromClause

    def __str__(self):
        expressions_str = ", ".join(str(e) for e in self.expressions)
        return f'select {expressions_str}'



class FromClause:
    def __init__(self, table, selectClause):
        self.table = table
        self.selectClause = selectClause
        
    def __str__(self):
        return  f"{str(self.selectClause)} from {self.table}"

    def where(self, expression):
        return WhereClause(expression, self)

class JoinClause:
    pass


class WhereClause:
    def __init__(self, expression, fromClause):
        self.expression = expression
        self.fromClause = fromClause

    def __str__(self):
        return f"{str(self.fromClause)} where {str(self.expression)}"


class GroupBy:
    pass


def select(*args):
    return SelectClause(*args)


def lit(value):
    pass


def lit_if_not_col(value):
    pass


class Expr:
    pass


class Column:
    def __init__(self, name) -> None:
        self.name = name
    
    def __eq__(self, __o: object):
        return EqCondition(self, __o)
    
    def __str__(self):
        return self.name


class EqCondition:
    def __init__(self, leftpart, rightpart):
        self.leftpart = leftpart
        self.rightpart = rightpart

    def __str__(self) -> str:
        return f"{self.leftpart} = '{self.rightpart}'"


class AndCondition(Expr):
    pass


class OrCondition(Expr):
    pass


class Table:
    def __init__(self, cls):
        self.table_cls = cls
        self.columns = {colname : Column(f"{self.table_cls.__name__.lower()}.{colname}") for colname in vars(cls) if not colname.startswith("__")}

    def __str__(self):
        return self.table_cls.__name__.lower()

    def __getattr__(self, item):
        return self.columns[item]


class CountAgg(Expr):
    pass


def table(cls):
    return Table(cls)


pattern = re.compile(r"( ){2,}")


def sql(query) -> str:
    return 


"""def distinct(col):
    return DistinctAgg(col)
"""

def count(col):
    pass
