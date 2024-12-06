c_or_f = input("Do you want to convert Celcius or Fahrenhiet? (F or C) = ")
if c_or_f == "F":
    fahr = int(input("Value of Fahrenhiet = "))
    fah_to_cel = 5/9 * (fahr - 32)
    print("Celcius = ", fah_to_cel)

elif c_or_f == "C":
    cel = int(input("Value of Celcius = "))
    cel_to_fah = (cel * 9 / 5) + 32
    print("Fahrenhiet = ", cel_to_fah)



