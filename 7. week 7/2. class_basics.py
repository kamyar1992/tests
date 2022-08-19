# class <class name> (object):
#   class body
import time


class kettle(object):
    # class attribute
    power = 'electric'

    # constructor
    def __init__(self, brand, price):
        # instance attributes
        self.brand = brand
        self.price = price
        self.on = False
        self.model = '2020'
        self.temperature = 15

    def turn_on(self):
        self.on = True

    def set_temperature(self, degree):
        while self.temperature < degree:
            self.temperature += 1
            time.sleep(1)
        print('the temperature is set to {}'.format(degree))


if __name__ == "__main__":
    smeg = kettle('Smeg', 5000000)  # instantiate (smeg is an instance of class kettle)
    pars_khazar = kettle('Pars Khasar', 2000000)

    print(smeg.price)
    print(pars_khazar.brand)
    print(pars_khazar.model)
    pars_khazar.model = "2022Alpha"
    print(pars_khazar.model)
    print(smeg.model)
    print(smeg.on)
    smeg.turn_on()
    print(smeg.on)
    # smeg.set_temperature(20)
    print('=' * 50)
#  namespaces:
#     print(smeg.__name__)
    print(smeg.__dict__)  # instance attributes
    print(kettle.__dict__)  # class attributes *important be careful instance and class attributes are totally different

    # class attributes are not in object attributes until an object chang it then it goes to that object name space
    # *important when a class attribute is change by an object, it just changes  for that instance not for all instances
    # and class
    print(kettle.power)
    print(smeg.power)
    pars_khazar.power = 'gas'
    print(pars_khazar.power)
    print(smeg.power)
    print(kettle.power)
    print('this is pars_khasar namespace: ', pars_khazar.__dict__)
    print('this is smeg namespace:      ', smeg.__dict__)
    print(help(type))
    print(dir())
    print(globals())
    print(smeg.__dict__)














