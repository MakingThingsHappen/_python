import pdb
from inspect import getsource


class MetaX(type):
    def __new__(meta, *args):
        print("__new__")
        print('meta: ', meta)
        print('args: ', args)
        x = type.__new__(meta, *args)
        print(getsource(x))
        return x

    def __init__(cls, what, bases=None, dict=None):
        print("__init__")
        print('cls: ', cls)
        print('what: ', what)
        print('bases: ', bases)
        print('dict: ', dict)
        type.__init__(cls, what, bases, dict)

    def __call__(cls, *args):
        print("__call__")
        print('cls: ', cls)
        print('args: ', args)
        x = type.__call__(cls, *args)
        print(getsource(x))
        return x


if __name__ == '__main__':
    print("*"*20, 'class', "*"*20)


    class A(object):
        __metaclass__ = MetaX

        def __call__(self, *args, **kwargs):
            print("__call__")
            return super(A, self).__call__(*args, **kwargs)

        def __init__(self, a, b):
            self.a = a
            self.b = b

    print("*"*20, 'instance', "*"*20)
    A(1, 2)

    # SM.__call__(A)

