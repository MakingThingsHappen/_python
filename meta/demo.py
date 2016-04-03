# -*- coding: utf-8 -*-


class Meta(type):
    def __new__(meta, class_name, supers, classdict):
        print("In Meta.__new__:\n"
              "meta:{0}\n"
              "class_name:{1}\n"
              "supers:{2}\n"
              "classdict:{3}".format(meta, class_name, supers, classdict))
        return type.__new__(meta, class_name, supers, classdict)


print("*"*20, "class define begin", "*"*20)


class Spam(object):
    __metaclass__ = Meta
    pass


print("*"*20, "class define end", "*"*20)


print("*"*20, "class instance begin", "*"*20)
s = Spam()
print("*"*20, "class instance end", "*"*20)
