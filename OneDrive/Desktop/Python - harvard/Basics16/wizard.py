class Wizard:
    def __init__(self , name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        ...

class Student(Wizard):
    def __init__(self , name ,house):
        super().__init(name)
        self.house = house
        
        ...
        
class Professor(Wizard):
    def __init__(self , name , subject):
        super().__init(name)
        self.subject = subject
        
        ...
        
wizard = Wizard("albus")
professor = Professor("severus" , "defense against the dark ages")     
student = Student("harry" , "gryffendor")