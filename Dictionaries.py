

""" the itemgetter fuction is imported
and tasks the value of N (5) """

from operator import itemgetter

obj = {}
file = open('textfile.txt')
sentence = file.readline()
sentence = sentence.split(" ")

for word in sentence:
    obj[word] = obj.get(word,0) + 1

obj['abc'] = 1
print(obj)

print(max(obj))



N = 5
""" will print the 5 most common words in testfile.ext """
res = dict(sorted(obj.items(), key=itemgetter(1), reverse=True)[:N])

print("the 5 most common words in the sentence are " + str(res)) 




