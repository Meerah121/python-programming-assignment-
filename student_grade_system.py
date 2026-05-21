def get_grade_and_point(score):
    """
    Returns the grade and grade point based on the score.
    """
    if 70 <= score <= 100:
        return 'A', 5
    elif 60 <= score <= 69:
        return 'B', 4
    elif 50 <= score <= 59:
        return 'C', 3
    elif 45 <= score <= 49:
        return 'D', 2
    elif 40 <= score <= 44:
        return 'E', 1
    else:
        return 'F', 0

def main():
    print("--- Student Grade System (GPA Calculator) ---")
    
    courses = []
    
    while True:
        course_name = input("Enter course name (or 'done' to calculate GPA): ")
        if course_name.lower() == 'done':
            break
            
        try:
            score = float(input(f"Enter score for {course_name}: "))
            credit_unit = int(input(f"Enter credit unit for {course_name}: "))
            
            grade, point = get_grade_and_point(score)
            print(f"Grade: {grade}\n")
            
            courses.append({
                'name': course_name,
                'point': point,
                'credit': credit_unit
            })
        except ValueError:
            print("Invalid input! Please enter numeric values for score and credit unit.")
            continue
            
    if not courses:
        print("No courses entered.")
        return
        
    total_grade_points = sum(c['point'] * c['credit'] for c in courses)
    total_credit_units = sum(c['credit'] for c in courses)
    
    if total_credit_units == 0:
        gpa = 0.0
    else:
        gpa = total_grade_points / total_credit_units
        
    print("-" * 30)
    print(f"Total Grade Points: {total_grade_points}")
    print(f"Total Credit Units: {total_credit_units}")
    print(f"Final GPA = {gpa:.1f}")

if __name__ == "__main__":
    main()
