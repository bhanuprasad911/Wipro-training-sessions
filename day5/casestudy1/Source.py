students =[]
faculty=[]
courses = []
class Person:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age
    def get_details(self):
        print(f"Name: {self.Name}, Age: {self.Age}")

class Student(Person):
    def __init__(self, id, Name, Age, dept, semester=1, marks=None, courses=None ):
        super().__init__(Name, Age)
        self.student_id = id
        self.semester = semester
        self.marks=marks if marks is not None else {}
        self.dept = dept
        self.courses = courses if courses is not None else []
        print("\n\n")
        print("Student added successfully")
        print("-"*30)
        print(f"ID         : {id}")
        print(f"Name       : {Name}")
        print(f"Department : {dept}")
        print(f"Semester   : {semester}")
        print("\n\n")
        
    def get_details(self):
        print("Student Details")
        print("-"*30)
        print(f'Name : {self.name}\nRole : Student\nDepartment : {self.dept}')
       
    def enroll(self, cid): 
        if cid in self.courses:
            print("The student has already enrolled in this course") 
            return
        course_found=False
        enrolledCourse=None
        for i in courses:
            if i.id==cid:
                enrolledCourse = i
                course_found = True
                break
        if course_found:
            self.courses.append(cid)
            print("\n\n")
            print("Enrollment Successfull")
            print('-'*30)
            print(f"Student name    : {self.Name}")
            print(f"Course enrolled : {enrolledCourse.Name}")
            print("\n\n")
        else:
            print("\nThere is no course with the given id, please try again with the correct id\n")
        
class Faculty(Person):
    def __init__(self, id, Name, Age, dept, salary):
        super().__init__(Name, Age)
        self.faculty_id = id
        self.salary = salary
        self.dept = dept
        print("\n\n")
        
        print("Faculty added successfully")
        print("-"*30)
        print(f"ID          : {id}")
        print(f"Name        : {Name}")
        print(f"Department  : {dept}")
        print("\n\n")
        
    def get_details(self):
        print("Faculty Details")
        print("-"*30)
        print(f'Name : {self.name}\nRole : Faculty\nDepartment : {self.dept}')

class Course:
    def __init__(self, id, Name, credits, faculty_name):
        self.id = id
        self.Name= Name
        self.credits = credits
        self.faculty_name=faculty_name
        print("\n\n")
        
        print("Course added successfully")
        print("-"*30)
        print(f"Course code: {id}")
        print(f"Course Name : {Name}")
        print(f"Credits: {credits}")
        print(f"Faculty: {faculty_name}")
        print("\n\n")
        

        '''
        1 → Add Student
2 → Add Faculty
3 → Add Course
4 → Enroll Student to Course
5 → Calculate Student Performance
6 → Compare Two Students
7 → Generate Reports
8 → Exit
'''


while True:
    print(f"1 -> Add Student \n2 -> Add Faculty \n3 -> Add Course \n4 -> Enroll student to course \n5 -> Get details \n6 -> Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        id = int(input("Enter Student id: "))
        is_student = False
        for i in students:
            if i.student_id == id:
                is_student = True
                break
        if is_student:
            print("\nA student already registered with the existing id, please try again..\n")
            continue
        Name = input("Enter Student Name: ")
        Age=int(input("Enter Student Age: "))
        dept = input("Enter Student department: ")
        semester = int(input("Enter semester: "))
        Student1 = Student(id, Name, Age, dept, semester)
        students.append(Student1)
        for i in students:
            print(i.Name)
        
    elif choice == 2:
        id = int(input("Enter faculty id: "))
        is_faculty = False
        for i in faculty:
            if i.faculty_id == id:
                is_faculty=True
                break
        if is_faculty:
            print("\nA faculty is already registered with the given id, please try again with another id\n")
            continue
                
        Name = input("Enter faculty Name: ")
        Age = int(input("Enter faculty Age: "))
        salary=int(input("Enter salary: "))
        dept = input("Enter department Name: ")
        new_faculty = Faculty(id, Name, Age, dept, salary)
        faculty.append(new_faculty)
        for i in faculty:
            print(i.Name)
    elif choice == 3:
        if not faculty:
            print("\nError: There are no faculty available, add faculty(option 2)\n")
            continue
        id = input("Enter course id: ")
        is_course=False
        for i in courses:
            if i.id==id:
                is_course = True
                break
        if is_course:
            print('\nA course has already registered with the given id, please try again with another id\n')
            continue
        Name = input("Enter Name: ")
        credits = int(input("Enter the number of credits: "))
        faculty_id=int(input("Enter faculty id: "))
        is_faculty = False
        for i in faculty:
            if i.faculty_id == faculty_id:
                is_faculty=True
                faculty_to_register = i
                break
        if is_faculty:
            faculty_name = faculty_to_register.Name
            new_course = Course(id, Name, credits, faculty_name)  
            courses.append(new_course)
            for i in courses:
                print(i.Name)
        else:
            print("\nThere is no faculty with the given id to assing the course\n")
    elif choice == 4:
        course_id = input("Enter course id to enroll: ")
        student_id = int(input("Enter student_id to be enrolled: )"))
        student_found = False
        for i in students:
            if student_id==i.student_id:
                student_to_be_enrolled = i
                student_found=True
                break
        if student_found:
            student_to_be_enrolled.enroll(course_id)
        else:
            print("\nThere is no student with the given id, please try again with the correct id\n")
    elif choice == 5:
        print("\nWhich details are to be fetched:")
        print("1 -> Student details \n2 -> Faculty details \n")
        ch = int(input("Enter your choice: "))
        print("Invalid input. Please enter a number.")
        if ch == 1:
            if not students:
                print("\nNo students available.\n")
                continue
            id = int(input("Enter Student id to fetch: "))
            found = False
            for s in students:
                if s.student_id == id:
                    s.get_details() 
                    found = True 
                    break
            if not found:
                print(f"\nThere is no student available with ID {id}\n")
        elif ch == 2:
            if not faculty:
                print("\nNo faculty members available.\n")
                continue
            id = int(input("Enter Faculty id to fetch: "))
            found = False
            for f in faculty:
                if f.faculty_id == id:
                    f.get_details()
                    found = True
                    break
            if not found:
                print(f"\nThere is no faculty available with ID {id}\n")
        else:
            print("\nInvalid sub-menu choice.\n")
    elif choice == 6:
        print("\nThank you for using Smart University Management System\n")
        break
    else:
        print("\ninvalid choice, please try again\n")
    