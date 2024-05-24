def display():
    #print("Hello world")
    return "Hello world"

#display() #calling function
print(display()) #printing what is returned

def evenOdd(number):
    return number%2 == 0

print(evenOdd(6))

def display_student(name, city): #pass as many variables, arguments I want
    #return "{} lives in {}".format(name, city)
    return {"name" : name, "City": city}

print(display_student("John", "Toronto"))


print("=====================================================================")
#===================================================================================#


def modify_list(numbers):
    tmp_numbers = numbers.copy() #create tmp array to avoid changing original value.
    numbers[0] = 100 #everything passed in argument is by reference so it will change original value. **be careful!!**
    return tmp_numbers

numbers = [1, 2, 3, 4, 5]
print(modify_list(numbers))

def get_max(numbers):
    # return max(numbers) - easier way
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max

numbers = [2, 1, 5, 3, 4]
print(get_max(numbers))

def is_palindrome(str):
    return str == str[::-1]

print(is_palindrome('racecar'))

print("=====================================================================")
#===================================================================================#

class Vehicle:
    '''
    # no need for the default constructor
    def __init__(self):
        self.name = None
        self.kms = 0
    '''
    # first parameter of function in a class always must be 'self'
    # self = current object.
    # no need to define the name, kms member data
    def __init__(self, name=None, kms=None): # constructor for python
        # this way, python will automatically create name and kms variable
        # you do not have to define the member data explicitly
        self.name = name # public by default
        #sef.__name = name - this is private now
        self.kms = kms

    def set_name(self, name):
        self.name = name
    
    def display(self):
        print("Name: {}, KMs: {}".format(self.name, self.kms))

v1 = Vehicle("Toyota", 123)
v1.display()
v1.name = "BMW"
v1.display()
v1.set_name("Honda")
v1.display()

print()
v2 = Vehicle()
v2.display()

print()
v3 = Vehicle("Hyundai") # single argument constructor
v3.display()

print()
print("Inheritance example")
class Car(Vehicle): #inheritance
    def __init__(self, name=None, kms=None, color=None):
        super().__init__(name, kms)
        self.color = color #there is no color in parent class so map it here
    
    def display(self):
        super().display()
        print("Color:", self.color)

car = Car("Toyota", 123, "White")
car.display()

print()

class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers
    def display(self):
        print(self.numbers)
    def get_max(self):
        return max(self.numbers)
    def get_min(self):
        return min(self.numbers)
    def get_sum(self):
        return sum(self.numbers)
    def get_avg(self):
        return sum(self.numbers)/len(self.numbers)
    def search(self, number):
        return number in self.numbers
    def even_numbers(self):
        #list comprehension
        return [evens for evens in self.numbers if evens%2]

numArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = Numbers(numArray)
print("Original Array :", numbers.display())
print("Max :", numbers.get_max())
print("Min :", numbers.get_min())
print("Sum :", numbers.get_sum())
print("Average :", numbers.get_avg(5))
print("Search :", numbers.search())
print("Even number :", numbers.even_numbers())
