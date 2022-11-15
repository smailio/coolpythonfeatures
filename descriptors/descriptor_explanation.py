from dataclasses import dataclass


@dataclass()
class Dude:
    name: str
    coolness: int


# class Leader:
#     """
#     This class is a descriptor as it implements the magic methods __get__ and __set___
#     """
#     def __get__(self, instance, owner):
#         print(f"""
#         Unlike when we access members here the default behavior of python is over-writen,
#         even if this instance {self} is accessed what is returned is the return value of
#         the __get__ function.
#         """)
#         return max(instance.members, key=lambda d: d.coolness)
#
#     def __set__(self, instance, value):
#         raise ValueError("Cant set the leader")


class DudeGang:
    def __init__(self, group_name):
        self.group_name = group_name
        self.members = []

    def join(self, dude):
        self.members.append(dude)

    # leader = Leader()
    # @property
    # def leader(self):
    #     return max(self.members, key=lambda d: d.coolness)


if __name__ == '__main__':
    # instantiate some dudes
    dudeA = Dude(name='Anis', coolness=1)
    dudeB = Dude(name='Dac', coolness=2)
    dudeC = Dude(name='Mouad', coolness=3)
    dudeD = Dude(name='Vincent', coolness=4)

    # oh no the dudes formed a gang
    gang = DudeGang('pythonistas')
    gang.join(dudeA)
    gang.join(dudeB)
    gang.join(dudeC)
    gang.join(dudeD)

    print("Normal access of the members instance attribute")
    print(gang.members)

    # # which one is the leader
    # print(gang.leader)
    #
    # dudeC.coolness = 1000
    # # it's over 999 !
    # print(gang.leader)


class Property(object):
    """
    This comes from Python's doc https://docs.python.org/3.7/howto/descriptor.html
    property descriptor is a built-in decorator, in CPython it's implemented directly in
    the interpreter, so it's coded in C in Objects/descrobject.c

    But this is a python version that emulatures the built-in property.
    """

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


