

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if '__inst' not in vars(cls):
            cls.__inst = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__inst


if __name__ == '__main__':
    a = Singleton()
    b = Singleton()
    print(a == b)

