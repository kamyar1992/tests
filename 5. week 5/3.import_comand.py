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

print(dir(myPackage.__init__))  # dir() just work for modules not packages
from myPackage.subpackage1 import subpackage_module1
print(subpackage_module1.subpackage1_module1())
print(dir(myPackage.subpackage1.__init__))

import PIL
print(dir(PIL.__init__))
print(dir(PIL))
help(PIL)

