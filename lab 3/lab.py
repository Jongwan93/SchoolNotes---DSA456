# Recursion, Searching and Sorting
# function calls itself

def factorial(n):
    if(n <= 1):
        return 1

    return n * factorial(n-1)

print(factorial(5))

def fibonacci(n):
    if(n<=1): #-------------------------------------O(1)
        return n #----------------------------------O(1)
    return fibonacci(n-1) + fibonacci(n-2) #--------O(1)

print(fibonacci(7))
#T(n) = O(n)

print()
print("===================================================================")
#=============================================================================
print()

