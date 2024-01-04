class Friedchicken:
    def __init__(self, name, time, size, money, smell):
        self.name = name
        self.time = time
        self.size = size
        self.money = money
        self.smell = smell

    def eatname(self):
        x = str(input('請點餐:'))
        self.name = x  
        print(f'我要{self.name}的')

    def eatsize(self):
        y = str(input('大中小要哪個:'))
        self.size = y
        print(f'{self.size}份')

    def taste(self):
        z = str(input('要加辣嗎:'))
        self.smell = z
        if(z == "要"):
            print('辣的')
        else:
            print('不辣')

# 建立4個物件
person1 = Friedchicken("醬燒", 20, "大", 200, "不辣")
person2 = Friedchicken("韓式", 25, "中", 150, "不辣")
person3 = Friedchicken("台式", 22, "小", 100, "不辣")
person4 = Friedchicken("清燙", 15, "中", 150, "不辣")

person1.eatname()  
person1.eatsize()  
person1.taste()
person1.money()