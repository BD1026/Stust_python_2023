class Area:
    def __init__(self,side,length,width,radius):
        self.side = side
        self.length = length
        self.width = width
        self.radius = radius

    def getSquareArea(self):
        print('正方形面積:',self.side**2)
        

    def getRectangleArea(self):
        print('長方形面積:',self.length*self.width)
        
    def getCircleArea(self):
        print('圓的面積:',self.radius*self.radius*3.14)

p1=Area(3,4,5,6)

p1.getSquareArea()
p1.getRectangleArea()
p1.getCircleArea()