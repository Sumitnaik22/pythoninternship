'''Write a program to calculate the grade.
    >= 90	--> Grade O
	>= 80	--> Grade A+
	>= 70	--> Grade A
	>= 60	--> Grade B+
	>= 50	--> Grade B
	 < 50	--> No Grade '''
score=int(input("Enter your score="))
if score not in range(1,101):
    print("Enter score between 1 and 100")
elif score>=90: print("grade is O")
elif score>=80:print("Grade is A+")
elif score>=70:print("Grade is A")
elif score>=60:print("Grade is B+")
elif score>=50:print("Grade is B")
else:print("No grade")