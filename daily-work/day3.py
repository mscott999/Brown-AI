class Student:
    def __init__(this, name, age):
        this.name = name
        this.age = age
    
    def printStudent(this):
        print("Name:", this.name, "\nAge: ", this.age)

class Course:
    def __init__(this, title, teacher, period):
        this.title = title
        this.teacher = teacher
        this.period = period
    
    def printCourse(this):
        print("Title:", this.title, "\nTeacher:", this.teacher, "\nPeriod:", this.period)

student1 = Student("Maddox Scott", 17)
student1.printStudent()
course1 = Course("Social Studies", "Mr. Teacher", 3)
course1.printCourse()