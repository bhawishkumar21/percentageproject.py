def calculate_percentage(marks_obtained, total_marks):
    if total_marks <= 0:
        return int(0)
    
    percentage = (marks_obtained / total_marks) * 100
    return percentage

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif 80 <= percentage < 90:
        return 'A'
    elif 70 <= percentage < 80:
        return 'B'
    elif 60 <= percentage < 70:
        return 'C'
    elif 50 <= percentage < 60:
        return 'D'
    else:
        return 'F'

marks_obtained = 429
total_marks = 550

percentage = calculate_percentage(marks_obtained, total_marks)
grade = calculate_grade(percentage)

print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
