import sqlite3

conn = sqlite3.connect('test_magic_methods_db.db')
_c = conn.cursor()
_c.execute('CREATE TABLE IF NOT EXISTS accounts (id text, balance real)')
_c.close()
conn.commit()

class myclassmethod:
    """Emulate PyClassMethod_Type() in Objects/funcobject.c"""

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        klass = type(obj)

        def newfunc(*args):
            return self.f(klass, *args)

        return newfunc


class mystaticmethod:
    """Emulate PyStaticMethod_Type() in Objects/funcobject.c"""

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f


class normal_method:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        def _f(*args):
            return self.f(obj, *args)
        return _f


class myproperty:
    def __init__(self, fun):
        self.fun = fun

    def __get__(self, instance, owner):
        return self.fun(instance)

    def __set__(self, instance, value):
        raise AttributeError("can't set this")


class mycachedproperty:
    def __init__(self, fun):
        self.fun = fun
        self.ret = None

    def __get__(self, instance, owner):
        if self.ret is None:
            self.ret = self.fun(instance)
        return self.ret

    def __set__(self, instance, value):
        raise AttributeError("can't set this")


class Account:
    def __init__(self, id):
        self.id = id
        c = conn.cursor()
        c.execute('SELECT * FROM accounts WHERE id=?', (id,))
        row = c.fetchone()
        if not row:
            c.execute('INSERT INTO accounts values (?, 0)', (id,))
            conn.commit()
            self.__balance = 0
        else:
            self.__balance = row[1]

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_val):
        self.__balance = new_val
        c = conn.cursor()
        c.execute("update accounts set balance = ? where id = ?", (new_val, self.id))
        conn.commit()
