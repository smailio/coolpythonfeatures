import sqlite3

conn = sqlite3.connect('test_magic_methods_db.db')
_c = conn.cursor()
_c.execute('CREATE TABLE IF NOT EXISTS accounts (id text, balance real)')
_c.close()
conn.commit()

class myclassmethod:
    """Emulate PyClassMethod_Type() in Objects/funcobject.c"""
    pass


class mystaticmethod:
    """Emulate PyStaticMethod_Type() in Objects/funcobject.c"""

    pass


class normal_method:
    pass


class myproperty:
    pass


class mycachedproperty:
    pass


class Account:
    pass
