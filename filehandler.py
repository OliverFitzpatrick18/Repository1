
stu_name = input("What is your name? = ")
stu_unit = input("What unit do you study? = ")
stu_mark = int(input("what mark did you get? = "))
stu_weight = int(input("what is your weight? = "))

if stu_mark <= 40:
    stu_grade = "Fail"
elif stu_mark <= 55:
    stu_grade = "Pass"
elif stu_mark <= 70:
    stu_grade = "Merit"
elif stu_mark <= 90:
    stu_grade = "Distiction"


file = open('answer.txt', 'a')

print(stu_name)
print(stu_mark)
print(stu_grade)

file.close()
