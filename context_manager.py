import os


class Cd:
    def __init__(self, dirname):
        self.dirname = dirname

    def __enter__(self):
        self.curdir = os.getcwd()
        os.chdir(self.dirname)

    def __exit__(self, type, value, traceback):
        os.chdir(self.curdir)


class Patch:
    def __init__(self, obj, **kwargs):
        self.obj = obj
        self.kwargs = kwargs
        self.obj_backup = {}

    def __enter__(self):
        for k in self.kwargs:
            self.obj_backup[k] = getattr(self.obj, k)
            setattr(self.obj, k, self.kwargs[k])

    def __exit__(self, type, value, traceback):
        for k in self.kwargs:
            setattr(self.obj, k, self.obj_backup[k])
