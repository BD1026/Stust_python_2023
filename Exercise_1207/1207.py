import re
from sys import stdout


class Fruit:
    def __init__(self, name:str):
        self.name = name

    @property
    def Fruit_name(self):
        print(f'"{self.name}"was accessed.')
        return self.name

    @Fruit_name.setter
    def Fruit_name(self,value):
        print(f'"{self.name}"is now "{value}".')
        self.name = value

    @Fruit_name.deleter
    def Fruit_name(self):
        print(f'"{self.name}"was deleted')
        del self.name


if __name__ == '__main__':
    fruit1 = Fruit('Banana')

    print(fruit1.Fruit_name)
    fruit1.Fruit_name = 'Apple'
    del fruit1.Fruit_name
    print(fruit1.Fruit_name)