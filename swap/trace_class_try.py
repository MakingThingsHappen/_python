# -*- coding: utf-8 -*-


class MetaX(type):
    def __new__(meta, classname, supers, classdict):
        print("__new__")
        print('meta: ', meta)
        print('classname: ', classname)
        print('supers: ', supers)
        print('classdict: ', classdict)
        x = type.__new__(meta, classname, supers, classdict)
        return x

    def __init__(cls, classname, supers, classdict):
        print("__init__")
        print('cls: ', cls)
        print('classname: ', classname)
        print('supers: ', supers)
        print('classdict: ', classdict)
        type.__init__(cls, classname, supers, classdict)


if __name__ == '__main__':
    print("*"*20, 'make class', "*"*20)

    class A(object):
        __metaclass__ = MetaX

        # def __call__(self, *args, **kwargs):
        #     print("__call__")
        #     return super(A, self).__call__(*args, **kwargs)

        def __init__(self, a, b):
            self.a = a
            self.b = b

    print("*"*20, 'make instance', "*"*20)
    A(1, 2)

    # SM.__call__(A)

