"""
This code contains some bugs and some errors.  
Find them and fix them.  
When you are done the program will print a message.
Write the message at the bottom of the code before submission
"""

#added def to defract_and_rearrange
#added _ inbetween str3
#changed string to str
#for str_3 remove the unnecesary Join(
#added a + before str_4
#fixedd typo on extract_and_rearrange
def extract_and_rearrange(str):
    str_1 = "".join(reversed(str[0:4].split('g'))).capitalize()
    str_2 = "".join(str[6:13].split('ro'))
    str_3 = "".join("".join(reversed(str[14:20])).split(str[17]))
    str_4 = "".join(str[21:29].split(str[23:28]))

    return str_1 + "" + str_2 + "" + str_3 + "" + str_4

#added : to ultra_extract_and_rearrange
#changed string to str on the first and second lines below 

def ultra_extract_and_rearrange(str):
    first_transform = extract_and_rearrange(str)
    return first_transform

#added _
#remove an unneccesary quote mark "
#fixed typo on ultra_extract_and_rearrange
print(ultra_extract_and_rearrange("egthb quirock nwoGrb forijmpxv"))

