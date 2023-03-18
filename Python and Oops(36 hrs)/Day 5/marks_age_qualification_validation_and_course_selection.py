class Student:
    def __init__(self):
        self.__att1=None
        self.__att2=None
        self.__att3=None
        self.__att5=None
    
    def set_attributes(self,student_id,marks,age,course):
        self.__att1=student_id
        self.__att2=marks
        self.__att3=age
        self.__att5=course
        
    def validate_marks(self):
        if(self.__att2 >= 65 and self.__att2 <=100):
            return True
        else:
            return False
    def validate_age(self):
        if(self.__att3 > 20):
            return True
        else:
            return False
    def check_qualification(self):
        if(self.__att2 >= 65 and self.__att3 >20):
            return True
        else:
            return False
        
    def choose_course(self):
        if  self.get_qualification():
            
            if(self.__att5==1001 and self.__att2>85):
                print(25575.0-(25575.0*0.25))
            elif(self.__att5==1001):
                print(25575.0)
            elif(self.__att5==1002 and self.__att2>85):
                print(15500-(15500.0*0.25))
            elif(self.__att5==1002):
                print(15500)
            else:
                print("No course is for you")
        else:
            print("Invalid")
    def get_marks(self):
        if(self.validate_marks()==True):
            return True
        else:
            return False
    def get_age(self):
        if(self.validate_age()==True):
            return True
        else:
            return False
    def get_qualification(self):
        if(self.check_qualification()==True):
            return True
        else:
            return False
    def get_id(self):
        return self.__att1
    def course_id(self):
        return self.__att5
    
    
    
student1 = Student()
student1.set_attributes(69,69,1,69)
print(student1.get_id())
print(student1.get_marks())
print(student1.get_age())
print(student1.get_qualification())
print(student1.course_id())
student1.choose_course()
