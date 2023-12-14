class Student:
    def __init__(self, Name, ID, Major):
        self.Name = Name
        self.ID = ID
        self.Major = Major
        


    def print_student_details(self):
        print(self.Name, self.ID, self.Major)

    def add_course(self, course):
        self.course = course
        print(f'{self.Name}選了{course}')

    def retreat(self, retreat):
        if(self.course == retreat):
            print(f'{retreat}已退選')

obj1 = Student("大A", 'C01', '資工')
obj2 = Student("小B", 'C02', '電機')

obj1.print_student_details()
obj2.print_student_details()


obj1.add_course('程式設計')
obj1.retreat('程式設計')
obj1.add_course('物件導向')
