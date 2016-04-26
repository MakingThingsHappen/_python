# -*- coding: utf-8 -*-
from __future__ import absolute_import


class A(type):
    def x(cls):
        print('ax', cls)

    def y(cls):
        print('ay', cls)


class B(metaclass=A):
    def y(self):
        print('by', self)

    def z(self):
        print('bz', self)


class A1(type):
    def a(cls):
        cls.x = cls.y + cls.z


class B1(metaclass=A1):
    y, z = 11, 22

    @classmethod
    def b(cls):
        return cls.x

if __name__ == '__main__':
    i = B1()
    print(i.x, i.y, i.z)

