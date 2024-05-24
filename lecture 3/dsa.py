# searching for the specific number in the numbers array
def search(numbers, num):
    pass

print(search([1, 2, 3, 4, 5], 1)) # best case scenario. because element looking for is the first one.
print(search([1, 2, 3, 4, 5], 5)) # worst case scenario. all elements has to be iterated
print(search([1, 2, 3, 4, 5], 6)) # worst case scenario. all elements has to be iterated
print(search([1, 2, 3, 4, 5], 3)) # average case scenario. not best but not worst

print()
print("===========================================================================")
#============================================================================================#
print()

def get_number(number):
    return number # O(1) because it is 'regular' python statement.

# what is the time complexity of get_number()? = O(1)
print(get_number(1))

# All regular statements, they are always going to run constant amount of time
    # when a logic is ran in a computer it will take different time to run depends on the computer spec.
    # so we set O(1), the constant time.
    # ex) 5 + 6 = 11 O(1) - "constant time" it will always take O(1) time when it is ran in a computer.
    # ex) if 5 < 6 (1 ms)
    # ex) return (1 ms)
    # len(numbers) O(1)

def get_number2(number):
    n = 100 # 0(1)
    return n # 0(1)

# what is the time complexity of get_number2()? = O(2) = O(1)
print(get_number(1000))
print()

def display(numbers): 
    for i in range(0, len(numbers)): # O(1)
        print(numbers[i])     # O(1)*n + O(1)*n **calling print function and numbers[i]**
    # for
        # 1. i = 0              O(1)
        # 2. i < len(numbers)   O(1)*n + O(1)*n **because len() is function**
        # 3. i++                O(1)*n
    # in this case for loop iterates n times.

# what is time complexity of display()? = O(25)
# assume the size of array is n.
# what is time complexity of display()? = O(4n + 1)
    # Rule 1 = Keep only fastest growing term = O(4n)
    # Rule 2 = Remove constants = O(n)

# therefore, time complexity of this function is O(n)
print(display([1, 2, 3, 4, 5]))

print()
print("===========================================================================")
#============================================================================================#
print()

def sum_of_elements(numbers): # size = n
    result = 0 # ----------------------------- O(1)
    for i in range(len(numbers)): # ---------- O(1) + O(1)*n + O(1)*n
        result += numbers[i] # --------------- O(1)*n + O(1)*n
    return result # -------------------------- O(1)

# O(1) + O(1) + O(1)*n + O(1)*n + O(1)*n + O(1)*n + O(1) = O(4n+3)
    # Rule 1 = O(3n)
    # Rule 2 = O(n)

# time complexity of this function based on the size of the array? = O(n)
print(sum_of_elements([1, 2, 3, 4, 5]))

print()
print("===========================================================================")
#============================================================================================#
print()

def display_pairs(numbers): # size = n
    for i in range(len(numbers)): # ------------------------------------ O(1) + O(1)*n + O(1)*n
        for j in range(len(numbers)): # -------------------------------- O(1)*n + O(1)*n + O(1)*n
            print("({}, {})".format(numbers[i], numbers[j]))# ---------- O(1)*n*n + O(1)*n*n + O(1)*n*n + O(1)*n*n

# time complexity of this function based on the size of the array? = **instead of this..**
# Use 'T(n) =' to write the answer where T = "Time"
# T(n) = 
display_pairs([1, 2, 3]) # (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), ...

# Step 1: Define variables
    # n is the size of the array
    # declare answer as T(n) which is the time complexity of the function

# Step 2:
    # find time complexity of each statement
    # you don't have to write answer of step 2 here again since its written on the code

# Step 3:
    # create mathematical equation
    # O(1) + O(1)*n + O(1)*n + O(1)*n + O(1)*n + O(1)*n + O(1)*n*n + O(1)*n*n + O(1)*n*n + O(1)*n*n
    # O(1) + O(n) + O(n) + O(n) + O(n) + O(n) + O(n^2) + O(n^2) + O(n^2) + O(n^2)

# Step 4: 
    # simplify the equation
    # O(1) + O(n) + O(n) + O(n) + O(n) + O(n) + O(n^2) + O(n^2) + O(n^2) + O(n^2) = O(1) + O(5n) + O(4n^2)
        # Rule 1 = Keep only fastest growing term = O(5n+1) + O(4n^2) = O(4n^2)
        # Rule 2 = Remove constants = O(4n^2) = O(n^2)
    # answer = O(n^2)

# Step 5:
    # final result
    # T(n) = O(n^2)
