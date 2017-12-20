#!/usr/bin/env python3

class animal(object):
   owner = 'Jack'
   count = 0
   def __init__(self , name = 'toy'):
    self.name = name
    self.count += 1

   def Get_owner(self):
    return self.owner

   def getcount(self):
    return self.count
   @classmethod
   def Get_num(cls):
    return cls.count



class Dog(animal):
   def __init__(self, name = 'wangcai'):
    self._name = name

   def GetName(self):
    return self._name

   def SetName(self, value):
    self._name = value

   def bark(self):
    print(self.GetName() + 'is making sound wang wang wang ...')


class Cat(animal):
   def __init__(self,name = 'kitty'):
    self.__name = name

   def GetName(self):
    return self.__name

   def SetName(self, value):
    self.__name = value

   def mew(self):
    print(self.GetName() + 'is making sound miu miu miu...')


cat = Cat()
print(cat.GetName())
print(cat.__name)
