# -*- coding: utf-8 -*-


class Cls(object):

    @classmethod
    def introduce(cls):
        print("Hello, I am %s!" %cls)


Cls.introduce()

# ---------------

class SubCls(Cls):
    pass


SubCls.introduce()

# ---------------

class Inst(object):

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, I am %s, and my name is %s" % (self, self.name))

myinst = Inst("Test Instance")
otherinst = Inst("An other instance")
myinst.introduce()
# outputs: Hello, I am <Inst object at x>, and my name is Test Instance
otherinst.introduce()
# outputs: Hello, I am <Inst object at y>, and my name is An other instance
# Inst.instance()
# AttributeError: type object 'Inst' has no attribute 'instance'