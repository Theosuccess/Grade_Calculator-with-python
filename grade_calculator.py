"""
assignment
GRADE CALCULATOR
input a score
70-100 A
60-69 B
50-59 C
45- 49 D
40-44E
0-39 F
"""

grade = int(input("enter a number: "))

if grade >= 70:
    amount = "A"
elif grade >= 60 and grade < 70:
    amount = "B"
elif grade >= 50 and grade < 60:
    amount = "C"
elif grade >= 45 and grade < 50:
    amount = "D"    
elif grade >= 40 and grade < 45:
    amount = "E"
elif grade >= 0 and grade < 40:
    amount = "F"
    
print (amount)



