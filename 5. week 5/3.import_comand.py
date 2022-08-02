import mod
print(mod.kamyar)

from mod import saba
print(saba)

from mod import saba as sb
print(sb)

from mod import *  # in big modules it creates problems and make a model or project heavy
print(test('hello'))  # pay attention to None that is printed
print('=' * 40)
# from myPackage import subpackage1,subpackage2
print('=' * 40)
import myPackage
print(myPackage.alist)
myPackage

