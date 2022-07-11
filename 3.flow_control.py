# Flow Control
# if elif esle ==> condition
# for else while ==> loops

# if :
age = 17
# chained conditioning
if age > 18:  # bool(age>18)
    print("sene ghanooni")
elif age > 15 and age <= 18:
    print("iekam moonde")
else:
    print('sene ghanooni nist')
print('='*40)
# unchained conditioning
if age > 18:  # bool(age>18)
    print("sene ghanooni")
if age > 15 and age <= 18:
    print("iekam moonde")
else:
    print('sene ghanooni nist')

if not age-18:  #important
    print("age is 18")
print('='*40)
# pep 20:
import this
print('='*40)
# ternary operator : *important
vote = True if age > 18 else False
print(vote)


temp = "some string"

myString = "ABc" if temp else "XYZ" # meanse if temp is not empety
print(myString)