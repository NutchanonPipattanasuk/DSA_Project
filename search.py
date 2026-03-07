import Database as db

def find_course(course_code):
    Data = db.Data
    if course_code in Data:
        print(f"Course Code : {course_code}")
        print(f"Name : {Data[course_code]['Name']}")
        print(f"Credit : {Data[course_code]['Credit']}")
        print(f"Lecturer : {', '.join(Data[course_code]['Lecturer'])}")
    
    else:
        print("Course not found")

    if __name__ == "__main__":
        find_course(course_code)

