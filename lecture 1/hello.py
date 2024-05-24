

first = "Seneca"
last = "College"

print("1.",first,last)
print("2.",first+last)   #concatnate
print("3. Result:", first, last)
print("4.",f"Hello, {first} {last}")
print("5.","Hello, {} {}".format(first, last))
print("============================================")

#===================================================================#

message = "          Seneca           "

print(message.upper())
print(message.lower())
print(message.title())
print(message.strip())
print(len(message)) #find length of the string
print("====================================================")

#=====================================================================#

i = 5
j = 6
a = 5.5
b = 6.2
result = i+j
result2 = a/b
print(i,j)
print(result)
print("Result:",result)
print(a)
print(result2)
print("Result: {} + {} = {}".format(a, b, result2)) #Result: 5.5 + 6.2 = 0.8870967741935484
print("Result: {} + {} = {:.2f}".format(a, b, result2)) #Result: 5.5 + 6.2 = 0.89
print("====================================================")

#=====================================================================#

num = 6
if(num % 2 == 0):
    print("Even")
    print("stupid")
else:
    print("Odd")

marks = 104
if(marks > 100):
    print("wrong input")
elif(marks >= 90):
    print("A")
elif(marks >= 80):
    print("B")
elif(marks >= 70):
    print("C")
elif(marks >= 60):
    print("D")
else:
    print("Fail")

first = "Seneca"
last = "College"

if (first == "Seneca" and last == "College"):
    print("I like it. Result: {} {}".format(first, last))
elif(first == "Seneca" or last == "College"):
    print("that is fine")
else:
    print("I don't like it")

if (first in "Seneca College Newnham"): # 'not in' is also possible
    print("I like it. Result: {}".format(first))
else:
    print("I don't like it")

num = 5
if(num != 5):
    print("Not a five!")

flag = True #must be True and False. case sensitive
if(not flag):
    print("it is false")
else:
    print("it is true")

print("====================================================")

#=====================================================================#

#num = input("Enter a number: ") #input returns string. so if you enter 4, it will return string "4"
num = int(input("Enter a number: ")) #cast it to integer

if(num % 2 == 0):
    print("Even")
else:
    print("Odd")

i = 1
while(i<=10):
    print(i, end=" ")
    i+=1
print()

prompt = input("Enter a fruit (q to quit): ")

while(True):    #while(prompt != "q")
    if(prompt == "q"):
        break
    prompt = input("Enter a fruit (q to quit): ")

for i in range(0, 10): #initial,end,step 
    # ** 10 is not included **
    print(i, end=" ")
print()
print("====================================================")

#=====================================================================#

#arrays
# arrays in python are called "Lists"
# int myArray = [1, 2, 3, 4] - this is C++ way
# myArray = [1, 2, 3, 4, "Apple"] - this is python way.
# python, you can input elements in different types to the array. Therefore it is called "List" instead of Array.
fruits = ["Apples", "Oranges", "Banana", "Grapes"]

print(fruits)
print(fruits[2])
#print(fruits[9]) - Error: out of range
print(fruits[-1]) #Grapes
print(fruits[-2]) #Banana
print(fruits[-3]) #Oranges
print(fruits[-4]) #Apples
print(fruits[0].upper())
fruits[0] = "PineApples"
print(fruits)
fruits.append("Shine Musket")
fruits.insert(2, "Blueberry")
fruits.remove("Oranges")
fruits.pop(1)   #?? what does it do?
print(fruits)
fruits.sort()
print(fruits)

nums = [2, 1, 7, 4, 6, 3, 5, 9, 8, 10]

for i in range(0, len(nums)):
    if(nums[i] % 2 == 0):
        print(nums[i],end = " ")
print()

for i in nums:
    if i % 2 == 0:
        print(i, end=" ")
print()

print(nums[:5]) #slicing
print(nums[2:5]) #range 2-5
print(nums[2:]) #range 2-end
print(nums[0:]) #everything
print(nums[::]) #everything
print(nums[0:-2]) #except last two
print(nums[0:10:2]) #from range 1-10, every second index
print(nums[::2]) #same from above
print(nums[::-1]) #reverse the array and print

print("====================================================")

#=====================================================================#

students = {
    "name": ["Steve", "John", "Bill"],
    "age": [30, 21, 20]}
print(students["name"][0]) #only print 'Steve' from the dictionary
print(students["name"][1])
print(students["age"][0])



