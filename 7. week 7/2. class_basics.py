# class <class name> (object):
#   class body
import time


class kettle(object):
    # class attribute

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
    smeg.set_temperature(20)





















