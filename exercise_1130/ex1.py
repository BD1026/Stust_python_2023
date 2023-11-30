class Student:
    def __init__(self,school,department,DepartmentChair,Name,ID,address,Fraction,score):
        self.school = school
        self.department = department
        self.DepartmentChair = DepartmentChair
        self.Name = Name
        self.ID = ID
        self.address = address
        self.Fraction = Fraction
        self.score = score

    def getschool(self):
        return self.school
        
    def setschool(self,newschool):
        self.school = newschool
        

    def getdepartment(self):
        return self.department

    def setdepartment(self,newdepartment):
        self.department = newdepartment

    def getDepartmentChair(self):
        return self.DepartmentChair

    def setDepartmentChair(self,newDepartmentChair):
        self.DepartmentChair = newDepartmentChair

    def getName(self):
        return self.Name

    def setName(self,newName):
        self.Name = newName

    def getID(self):
        return self.ID

    def setID(self,newID):
        self.ID = newID

    def getaddress(self):
        return self.address

    def setaddress(self,newaddress):
        self.address = newaddress
    
    def getFraction(self):
        return self.Fraction

    def setFraction(self,newFraction):
        self.Fraction  = newFraction

    def getscore(self):
        return self.score

    def setscore(self,newscore):
        self.score = newscore

#建立副函式
person1 = Student("STUST","資訊工程","洪國鈞","朱延鈺","4B0G0028","高雄市",120,90)

print(person1.getschool())
print(person1.getdepartment())
print(person1.getDepartmentChair())
print(person1.getName())
print(person1.getID())
print(person1.getaddress())
print(person1.getFraction())
print(person1.getscore())