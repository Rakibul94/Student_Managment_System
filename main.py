#OOP Design (Both Student and Course class)

class Course:
    def __init__(self, course_name):
        self.course_name = course_name




class Student:
    def __init__(self, name, roll, password):
        self.name = name
        self.roll = roll
        self.courses = []
        self.__password = password   # Encapsulation (private instance variable)

    def enroll_course(self, course):
        self.courses.append(course.course_name)
        self.save_to_file(course.course_name)

    #File Handling (ALL student data will be saved in students.txt file)

    def save_to_file(self, course_name):
        with open("students.txt", "a") as file:
            file.write(f"Name: {self.name}, Roll: {self.roll}, Course: {course_name}\n")

    #Private instance can only be accessed using getter method
    def get_password(self):
        return self.__password
    
# Read Data
def show_all_students():
    #Exception Handling (For error incase student.txt was never created)
    try:
        with open("students.txt", "r") as file:
            print("All Students:")
            for s in file:
                print(s.strip())
    except FileNotFoundError:
        print("No Data Found.")



#Creating Student Objects

student1 = Student("Md Rakibul Islam", 1314, "protect456")
student2 = Student("Shahriar Hossain", 1210, "leakproof123")


#Creating Course Objects

student1.enroll_course(Course("Cybersecurity"))
student1.enroll_course(Course("Machine Learning"))
student2.enroll_course(Course("Data Science"))

#Password can be accessed using only getter method,it cannot be accessed directly by calling objects
print("Student Password:", student1.get_password()) 
print("Student Password:", student2.get_password())

#Calling this function to show all students from the file
show_all_students()




