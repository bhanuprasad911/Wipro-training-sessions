import json
import csv

# --- CLASSES ---

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
        self.marks = marks if marks is not None else {}
        self.dept = dept
        self.courses = courses if courses is not None else []
        print("\nStudent added successfully")
        print("-" * 30)
        
    def obj_to_dict(self):
        return {
           "id": self.student_id,
           "Name": self.Name,
           "Age": self.Age,
           "dept": self.dept,
           "semester": self.semester,
           "marks": self.marks,
           "courses": self.courses
        }

    def get_details(self):
        print("\n" + "-"*30)
        print("Student Details")
        print("-"*30)
        print(f"ID         : {self.student_id}")
        print(f'Name       : {self.Name}')
        print(f'Role       : Student')
        print(f'Department : {self.dept}')
        print(f'Enrolled   : {self.courses}')
        print("-" * 30 + "\n")
       
    def enroll(self, cid, courses): 
        if cid in self.courses:
            print("\nError: The student has already enrolled in this course.\n") 
            return
        
        # Check if course exists in the global list (passed logically)
        course_found = False
        enrolledCourse = None
        
        # Note: In a real app, pass 'courses' list as an argument. 
        # Here we access the global 'courses' variable.
        for i in courses:
            if i.id == cid:
                enrolledCourse = i
                course_found = True
                break
        
        if course_found:
            self.courses.append(cid)
            print("\n" + "-"*30)
            print("Enrollment Successful")
            print(f"Student name    : {self.Name}")
            print(f"Course enrolled : {enrolledCourse.Name}")
            print("-" * 30 + "\n")
        else:
            print(f"\nError: Course ID '{cid}' not found.\n")

    def addMarks(self, subject, marks):
        self.marks[subject] = marks
        print(f"Marks added successfully: {subject} -> {marks}")

    # Helper method to get average for internal use
    def get_average(self):
        if not self.marks:
            return 0.0
        return sum(self.marks.values()) / len(self.marks)

    # OPERATOR OVERLOADING (>): To compare two students based on average
    def __gt__(self, other):
        return self.get_average() > other.get_average()

    def fetch_performance(self):
        if not self.marks:
            print(f"\nNo marks available for {self.Name}.\n")
            return

        iter_data = iter(self.marks.values())
        total_sum = 0
        count = 0
        
        while True:
            try:
                number = next(iter_data)
                total_sum += number
                count += 1
            except StopIteration:
                break
        
        if count == 0:
            avg = 0
        else:
            avg = total_sum / count
            
        grade = ""
        if avg >= 85: grade = "A"
        elif 85 > avg >= 65: grade = "B"
        elif 65 > avg >= 55: grade = "C"
        elif 55 > avg >= 40: grade = "D"
        else: grade = "F"
        
        print("\n" + "-"*30)
        print("Student Performance Report")
        print("-" * 30)
        print(f"Student Name: {self.Name}")
        print(f"Marks       : {self.marks}")
        print(f"Average     : {avg:.2f}")
        print(f"Grade       : {grade}")
        print("-" * 30 + "\n")
    
        
class Faculty(Person):
    def __init__(self, id, Name, Age, dept, salary):
        super().__init__(Name, Age)
        self.faculty_id = id
        self.salary = salary
        self.dept = dept
        print("\nFaculty added successfully")
        print("-" * 30)
        
    def get_details(self):
        print("\n" + "-"*30)
        print("Faculty Details")
        print("-"*30)
        print(f"ID         : {self.faculty_id}")
        print(f'Name       : {self.Name}')
        print(f'Role       : Faculty')
        print(f'Department : {self.dept}')
        print("-" * 30 + "\n")

class Course:
    def __init__(self, id, Name, credits, faculty_name):
        self.id = id
        self.Name = Name
        self.credits = credits
        self.faculty_name = faculty_name
        print("\nCourse added successfully")
        print("-" * 30)
        
    def get_details(self):
        print("\n" + "-"*30)
        print("Course Details")
        print("-"*30)
        print(f"ID          : {self.id}")
        print(f"Course Name : {self.Name}")
        print(f"Credits     : {self.credits}")
        print(f"Faculty     : {self.faculty_name}")
        print("-" * 30 + "\n")