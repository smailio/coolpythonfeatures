import os

class Cd:
    def __init__(self, dirname):
        self.dirname = dirname

    def __enter__(self):
        self.curdir = os.getcwd()
        os.chdir(self.dirname)

    def __exit__(self, type, value, traceback):
        os.chdir(self.curdir)


import copy

class Patch:
    def __init__(self, target, **kwargs):
        self.target = target
        self.kwargs = kwargs
        self.saved_values = {}

    def __enter__(self):
        for attr, value in self.kwargs.items():
            self.saved_values[attr] = copy.copy(getattr(self.target, attr))
            setattr(self.target, attr, value)

    def __exit__(self, etype, value, traceback):
        for attr, value in self.saved_values.items():
            setattr(self.target, attr, value)
