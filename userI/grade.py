marks=float(input("Enter student's marks: "))
if marks >= 90 and marks <= 100: # 90 - 100
    print("grade A+")
    
elif marks >= 80 and marks < 90: # 80 - 89
    print("Grade: A")
elif marks >= 70 and marks < 80: # 70 - 79
    print("Grade: B")
elif marks >= 60 and marks < 70:   #60-69    
    print("Grade: C")
elif marks >= 50 and marks < 60: #50-59
    print("Grade: D")
elif marks >= 0 and marks < 50: #0-49
    print("Grade: Fail")
else:
    print("Invalid marks entered. Please enter marks between 0 and 100.")    

