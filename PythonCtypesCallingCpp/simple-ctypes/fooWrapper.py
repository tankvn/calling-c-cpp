from ctypes import cdll
#lib = cdll.LoadLibrary('./libfoo.so')
lib = cdll.LoadLibrary('./robot_control_interface_dnwa.so')

class Foo(object):
    def __init__(self):
        self.obj = lib.Foo_new()

    def bar(self):
        lib.Foo_bar(self.obj)

f = Foo()
f.bar() #and you will see "Hello" on the screen