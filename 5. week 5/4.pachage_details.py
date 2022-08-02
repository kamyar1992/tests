# packages
# this import does not work
# import myPackage
# myPackage.module1.fun1()
import myPackage.subpackage1
import myPackage.subpackage2
from myPackage import module1
module1.fun1()

from myPackage.module2 import modul2String
print(modul2String)


from myPackage.module1 import modul1String as s1
print(s1)


from myPackage.module2 import fun2
fun2()

from myPackage.subpackage1 import subpackage_module1
subpackage_module1.subpackage1_module1()