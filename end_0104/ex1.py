class Friedchicken:
    def __int__ (self, name, time, size, money, smell):
        self.name = name
        self.time = time
        self.size = size
        self.money = money
        self.smell = smell

    def order():
        while True:
            choice = int(input("請選擇想點餐的編號 (1-4)，退出請按0: "))

            if choice == 0:
                print("謝謝惠顧，歡迎下次光臨！")
                break

            elif choice == 1:
                person1.eatname()
                person1.eatsize()
                person1.taste()

            elif choice == 2:
                person2.eatname()
                person2.eatsize()
                person2.taste()

            elif choice == 3:
                person3.eatname()
                person3.eatsize()
                person3.taste()

            elif choice == 4:
                person4.eatname()
                person4.eatsize()
                person4.taste()

    def eatname(self):
        x = str(input('請點餐:'))
        print(f'我要{x}的')

    def eatsize(self):
        print(f'{self.size}份')

    def taste(self):
        print(f'是{self.smell}的')


    

# 建立4個物件
person1 = Friedchicken("醬燒", 20, "大", 200, "辣")
person2 = Friedchicken("韓式", 25, "中", 150, "辣")
person3 = Friedchicken("台式", 22, "小", 100, "不辣")
person4 = Friedchicken("清燙", 15, "中", 150, "不辣")

print.order()
