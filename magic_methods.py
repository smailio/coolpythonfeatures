import re


class SelectClause:
    def __init__(self, columns):
        self.columns = columns

    def frm(self, t):
        return FromClause(self, t)

    def __str__(self):
        return "select " + ", ".join(str(col) for col in self.columns)


class FromClause:
    def __init__(self, select_clause, t):
        self.select_clause = select_clause
        self.table = t

    def join(self, t, condition):
        return JoinClause(self, t, condition)

    def where(self, condition):
        return WhereClause(self, condition)

    def __str__(self):
        return str(self.select_clause) + f" from {str(self.table)}"

    def group_by(self, *exprs):
        return GroupBy(self, *exprs)


class JoinClause:
    def __init__(self, from_clause, t, condition):
        self.from_clause = from_clause
        self.table = t
        self.condition = condition

    def join(self, t, condition):
        return JoinClause(self, t, condition)

    def where(self, condition):
        return WhereClause(self, condition)

    def __str__(self):
        return (
            str(self.from_clause)
            + f" join {str(self.table)} on {str(self.condition)}"
        )


class WhereClause:
    def __init__(self, from_clause, condition):
        self.from_clause = from_clause
        self.condition = condition

    def __str__(self):
        return str(self.from_clause) + " where" + str(self.condition)

    def group_by(self, *exprs):
        return GroupBy(self, *exprs)


class GroupBy:
    def __init__(self, clause, *exprs):
        self.clause = clause
        self.exprs = exprs

    def __str__(self):
        return str(self.clause) + " group by " + ",".join(str(e) for e in self.exprs)


def select(*args):
    return SelectClause(lit_if_not_col(arg) for arg in args)


def lit(value):
    if isinstance(value, str):
        value = f"'{value}'"
    return Column(str(value))


def lit_if_not_col(value):
    if isinstance(value, Column):
        return value
    if isinstance(value, Expr):
        return value
    else:
        return lit(value)


class Expr:
    def __eq__(self, other):
        return EqCondition(self, lit_if_not_col(other))

    def __and__(self, other):
        return AndCondition(self, lit_if_not_col(other))

    def __or__(self, other):
        return OrCondition(self, lit_if_not_col(other))


class Column(Expr):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class EqCondition(Expr):
    def __init__(self, col1, col2):
        self.col1 = col1
        self.col2 = col2

    def __str__(self):
        return " " + str(self.col1) + " = " + str(self.col2)


class AndCondition(Expr):
    def __init__(self, col1, col2):
        self.col1 = col1
        self.col2 = col2

    def __str__(self):
        return " (" + str(self.col1) + " and" + str(self.col2) + " )"


class OrCondition(Expr):
    def __init__(self, col1, col2):
        self.col1 = col1
        self.col2 = col2

    def __str__(self):
        return " ( " + str(self.col1) + " or " + str(self.col2) + " )"


class Table:
    def __init__(self, cls):
        self.cls = cls
        self.columns = {
            name: Column(cls.__name__.lower() + "." + name)
            for name in vars(cls)
            if not name.startswith("__")
        }

    def __getattr__(self, item):
        return self.columns[item]

    def __str__(self):
        return self.cls.__name__.lower()




class CountAgg(Expr):
    def __init__(self, col):
        self.col = col

    def __str__(self):
        return " count(" + str(self.col) + ")"


def table(cls):
    return Table(cls)


pattern = re.compile(r"( ){2,}")


def sql(query) -> str:
    return re.sub(pattern, " ", query.sql())


"""def distinct(col):
    return DistinctAgg(col)
"""

def count(col):
    return CountAgg(col)
