import mod
print(mod.kamyar)

from mod import saba
print(saba)

from mod import saba as sb
print(sb)

from mod import *  # in big modules it creates problems and make a model or project heavy
print(test('hello'))

