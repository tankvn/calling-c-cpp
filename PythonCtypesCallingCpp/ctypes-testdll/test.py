import os
from ctypes import *

#lib = cdll.LoadLibrary(os.path.join(os.path.abspath('.'), r'testDLL\build\Win32\Release\testDLL.dll'))
lib = windll.LoadLibrary(os.path.join(os.path.abspath('.'), r'testDLL\build\x64\Release\testDLL.dll'))

lib.testDLL(3)