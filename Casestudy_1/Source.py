import json
import csv
from Classes import Student, Faculty, Course

# --- GLOBAL LISTS ---
students = []
faculty = []
courses = []

# --- MAIN MENU ---

while True:
    print("\n" + "="*40)
    print(" SMART UNIVERSITY MANAGEMENT SYSTEM")
    print("="*40)
    print("1 -> Add Student") 
    print("2 -> Add Faculty") 
    print("3 -> Add Course") 
    print("4 -> Enroll Student to Course") 
    print("5 -> Get Details (Student/Faculty/Course)") 
    print("6 -> Add Marks") 
    print("7 -> Calculate Performance") 
    print("8 -> Compare Two Students") 
    print("9 -> Generate CSV Report")
    print("10 -> Save Data to JSON")
    print("11 -> Exit")
    print("-" * 40)
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # --- 1. ADD STUDENT ---
    if choice == 1:
        print("\n--- Add Student Menu ---")
        print("1. Manual Entry")
        print("2. Load from JSON file")
        sub_choice = input("Enter option (1 or 2): ")

        if sub_choice == "1":
            try:
                id = int(input("Enter Student id: "))
            except ValueError:
                print("Invalid ID format.")
                continue

            # Check duplication
            is_student = False
            for i in students:
                if i.student_id == id:
                    is_student = True
                    break
            
            if is_student:
                print(f"\nError: Student ID {id} already exists.\n")
                continue
                
            Name = input("Enter Student Name: ")
            Age = int(input("Enter Student Age: "))
            dept = input("Enter Student department: ")
            semester = int(input("Enter semester: "))
            
            Student1 = Student(id, Name, Age, dept, semester)
            students.append(Student1)

        elif sub_choice == "2":
            file_name = input("Enter the JSON file name (e.g., students.json): ")
            try:
                with open(file_name, 'r') as file:
                    data = json.load(file)
                    added_count = 0
                    skipped_count = 0
                    for item in data:
                        s_id = item['id']
                        already_exists = False
                        for s in students:
                            if s.student_id == s_id:
                                already_exists = True
                                break
                        if already_exists:
                            skipped_count += 1
                            continue
                        
                        new_student = Student(
                            id=s_id, 
                            Name=item.get('Name', 'Unknown'), 
                            Age=item.get('Age', 0), 
                            dept=item.get('dept', 'General'), 
                            semester=item.get('semester', 1),
                            marks=item.get('marks', None),
                            courses=item.get('courses', None)
                        )
                        students.append(new_student)
                        added_count += 1
                    print(f"\nSuccess: Added {added_count}. Skipped {skipped_count}.\n")
            except Exception as e:
                print(f"\nError loading file: {e}\n")
        
    # --- 2. ADD FACULTY ---
    elif choice == 2:
        id = int(input("Enter faculty id: "))
        is_faculty = False
        for i in faculty:
            if i.faculty_id == id:
                is_faculty=True
                break
        if is_faculty:
            print("\nError: Faculty ID already exists.\n")
            continue
                
        Name = input("Enter faculty Name: ")
        Age = int(input("Enter faculty Age: "))
        salary = int(input("Enter salary: "))
        dept = input("Enter department Name: ")
        new_faculty = Faculty(id, Name, Age, dept, salary)
        faculty.append(new_faculty)

    # --- 3. ADD COURSE ---
    elif choice == 3:
        if not faculty:
            print("\nError: Add Faculty first (Option 2).\n")
            continue
        id = input("Enter course id: ")
        
        is_course = False
        for i in courses:
            if i.id == id:
                is_course = True
                break
        if is_course:
            print('\nError: Course ID already exists.\n')
            continue
            
        Name = input("Enter Name: ")
        credits = int(input("Enter credits: "))
        faculty_id = int(input("Enter faculty id for this course: "))
        
        is_faculty = False
        faculty_to_register = None
        for i in faculty:
            if i.faculty_id == faculty_id:
                is_faculty = True
                faculty_to_register = i
                break
        
        if is_faculty:
            faculty_name = faculty_to_register.Name
            new_course = Course(id, Name, credits, faculty_name)  
            courses.append(new_course)
        else:
            print("\nError: Faculty ID not found.\n")

    # --- 4. ENROLL STUDENT ---
    elif choice == 4:
        if not students: 
            print("No students available.")
            continue
        student_id = int(input("Enter student_id to be enrolled: "))
        course_id = input("Enter course id to enroll: ")
        
        student_found = False
        student_to_be_enrolled = None
        for i in students:
            if student_id == i.student_id:
                student_to_be_enrolled = i
                student_found = True
                break
        if student_found:
            student_to_be_enrolled.enroll(course_id, courses)
        else:
            print("\nStudent ID not found.\n")

    # --- 5. GET DETAILS ---
    elif choice == 5:
        print("\nWhich details are to be fetched:")
        print("1 -> Student details")
        print("2 -> Faculty details")
        print("3 -> Course details")
        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            continue

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
            if not found: print(f"Student ID {id} not found.")

        elif ch == 2:
            if not faculty:
                print("\nNo faculty available.\n")
                continue
            id = int(input("Enter Faculty id to fetch: "))
            found = False
            for f in faculty:
                if f.faculty_id == id:
                    f.get_details()
                    found = True
                    break
            if not found: print(f"Faculty ID {id} not found.")

        elif ch == 3:
            if not courses:
                print("\nNo courses available.\n")
                continue
            id = input("Enter Course ID to fetch: ")
            found = False
            for c in courses:
                if c.id == id:
                    c.get_details()
                    found = True
                    break
            if not found: print(f"Course ID {id} not found.")

    # --- 6. ADD MARKS ---
    elif choice == 6: 
        if not students:
            print("\nNo students available.\n")
            continue
        
        studentId = int(input("Enter Student id to enter the marks: "))
        found = False
        student = None 
        
        for s in students:
            if s.student_id == studentId:
                found = True 
                student = s 
                break
        
        if found:
            try:
                subject_count = int(input("Enter how many subjects you want to add: "))
                for i in range(subject_count):
                    subject_id = input("Enter course Id: ")
                    # Enforce enrollment check
                    if subject_id not in student.courses:
                        print(f"Error: Student is not enrolled in '{subject_id}'. Marks rejected.")
                    else:
                        marks = int(input(f"Enter marks for {subject_id}: "))
                        if 0 <= marks <= 100:
                            student.addMarks(subject_id, marks)
                        else:
                            print("Error: Marks should be between 0 and 100.")
            except ValueError:
                print("Invalid input.")
        else:
            print("\nStudent not found.\n")

    # --- 7. CALCULATE PERFORMANCE ---
    elif choice == 7:
        if not students:
            print("\nNo students available.\n")
            continue
        
        s_id = int(input("Enter Student ID to calculate performance: "))
        found = False
        for s in students:
            if s.student_id == s_id:
                s.fetch_performance()
                found = True
                break
        if not found:
            print("Student ID not found.")

    # --- 8. COMPARE STUDENTS (OPERATOR OVERLOADING) ---
    elif choice == 8:
        if len(students) < 2:
            print("\nNeed at least 2 students to compare.\n")
            continue
            
        id1 = int(input("Enter First Student ID: "))
        id2 = int(input("Enter Second Student ID: "))
        
        s1 = next((s for s in students if s.student_id == id1), None)
        s2 = next((s for s in students if s.student_id == id2), None)
        
        if s1 and s2:
            print("\n" + "-"*30)
            print(f"Comparing {s1.Name} vs {s2.Name}")
            print(f"{s1.Name} Average: {s1.get_average():.2f}")
            print(f"{s2.Name} Average: {s2.get_average():.2f}")
            
            # Uses the __gt__ method defined in Student class
            if s1 > s2:
                print(f"Result: {s1.Name} has a higher average.")
            elif s2 > s1:
                print(f"Result: {s2.Name} has a higher average.")
            else:
                print("Result: Both students have the same average.")
            print("-" * 30 + "\n")
        else:
            print("One or both Student IDs not found.")

    # --- 9. GENERATE CSV REPORT ---
    elif choice == 9:
        if not students:
            print("No data to generate report.")
            continue
        
        filename = "students_report.csv"
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['ID', 'Name', 'Department', 'Semester', 'Average_Marks']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for s in students:
                    writer.writerow({
                        'ID': s.student_id,
                        'Name': s.Name,
                        'Department': s.dept,
                        'Semester': s.semester,
                        'Average_Marks': f"{s.get_average():.2f}"
                    })
            print(f"\nReport generated successfully: {filename}\n")
        except Exception as e:
            print(f"Error generating CSV: {e}")

    # --- 10. SAVE DATA TO JSON ---
    elif choice == 10:
        if not students:
            print("No data to save.")
            continue
        file_name = input("Enter filename to save (e.g., final_data.json): ")
        
        data_to_save = []
        for s in students:
            data_to_save.append(s.obj_to_dict())
            
        try:
            with open(file_name, 'w') as file:
                json.dump(data_to_save, file, indent=4)
            print(f"\nSuccessfully saved {len(data_to_save)} students to {file_name}\n")
        except Exception as e:
            print(f"Error saving file: {e}")

    # --- 11. EXIT ---
    elif choice == 11:
        print("\nThank you for using Smart University Management System. Goodbye!\n")
        break
    else:
        print("\nInvalid choice, please try again\n")