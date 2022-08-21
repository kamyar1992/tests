# dock typing:

class Duck(object):

    @staticmethod
    def walk():
        print('I walk as duck')

    @staticmethod
    def quack():
        print('quack quack !!!!')

    @staticmethod
    def swim():
        print('I can swim')


# dock typing:

class Penguin(object):

    @staticmethod
    def walk():
        print("I don't walk as duck")

    @staticmethod
    def quack():
        print("I don't quack quack !!!!")

    @staticmethod
    def swim():
        print('I can swim very fast!!!!')


def bird(bird_object):
    bird_object.swim()
    bird_object.walk()
    bird_object.quack()


if __name__ == "__main__":
    duck = Duck()
    penguin = Penguin()

    bird(duck)
    bird(penguin)


