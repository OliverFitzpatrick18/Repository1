number_one = int(input("enter a number here = "))
number_two = int(input("enter another number here = "))

number_sum = number_one + number_two

if number_one > number_two:
    number_difference = number_one - number_two
elif number_one < number_two:
    number_difference = number_two - number_one

print("the sum of the two numbers is ", number_sum)
print("the difference between the two numbers is", number_difference)
