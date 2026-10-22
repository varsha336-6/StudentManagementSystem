English=78
Math=90
Science=85
print("English:", English)
print("Math:", Math)
print("Science:", Science)
total_marks = English + Math + Science
print("Total Marks:", total_marks)
average_marks = total_marks / 3
print("Average Marks:", average_marks)
if average_marks >= 90:
    print("Grade: A")
elif average_marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")
    