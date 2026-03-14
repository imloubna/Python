name=['GILL','ABI','RAHUL','JOHN','ANU']
marks=[[30,40,50],[67,88,90],[10,20,30],[90,76,67],[80,70,60]]

for i in range(len(name)):
    total = sum(marks[i])
    percentage = total / 3

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 60:
        grade = "A"
    elif percentage >= 40:
        grade = "B"
    else:
        grade = "F"

    print(name[i],"-", "Percentage:", percentage, "Grade:", grade)
    




