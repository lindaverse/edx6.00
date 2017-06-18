#Exercise - hello world
print("hello world")


#Exercise - happy
happy = 2

if happy > 2:
    print("hello world")

#Exercise - vara varb
varA = 1
varB = 1

if type(varA) == str and type(varB) == str:
    print("string involved")
else:
    if varA > varB:
        print("bigger")
    elif varA == varB:
        print("equal")
    elif varA < varB:
        print("smaller")

#1. Convert the following into code that uses a while loop.
#print 2
#prints 4
#prints 6
#prints 8
#prints 10
#prints Goodbye!

#num = 0
#while num <= 8:
    #num += 2
    #print(num)
#print("Goodbye!")


for i in range(2, 12, 2):
    print(i)
print("Goodbye!")

#2. Convert the following into code that uses a while loop.
#prints Hello!
#prints 10
#prints 8
#prints 6
#prints 4
#prints 2


# num = 10

#print("Hello!")
#while num >= 10:
    #print(num)
    #num -= 2

print("Hello!")
for i in range(10, 0, -2):
    print(i)

#3. Write a while loop that sums the values 1 through end, inclusive.
# end is a variable that we define for you.
# So, for example, if we define end to be 6, your code should print out the result:
#21
#which is 1 + 2 + 3 + 4 + 5 + 6.

#For problems such as these, do not include input statements or define variables we will provide for you.
# Our automating testing will provide values so write your code in the following box assuming these
# variables are already defined.

end = 6
result = 0

while end > 0:
    result += end
    end -= 1
print(result)

end = 6
result = 0
for i in range(end):
    result += end
    end -= 1
print(result)


greeting = 'Hello!'
count = 0

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print("numCons: " + str(numCons))
print("numVowels: " + str(numVowels))

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 