def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number-1) + fibonacci(number-2)

print(fibonacci(7))


def factorial(number):
    if number <= 1:
        return number
    return number*factorial(number-1)

print(factorial(4))

def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)-i-1):
            if numbers[j] > numbers[j+1]:
                tmp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1]=tmp
    return numbers

print(bubble_sort([4, 1, 6, 2, 5, 3, 7]))

def selection_sort(numbers):
    for i in range(len(numbers)):
        index = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[index]:
                index = j
        # tmp = numbers[i]
        # numbers[i] = numbers[index]
        # numbers[index] = tmp
        if i != index:
            numbers[i], numbers[index] = numbers[index], numbers[i]
    return numbers
    # T(n) = O(n^2)

print(selection_sort([4, 2, 5, 1, 6, 2, 4, 3]))

def quick_sort1(numbers):
    if len(numbers) <= 1:
        return numbers
    
    pivot = numbers[len(numbers)//2]
    smaller_arr, equal_arr, larger_arr = [], [], []
    for num in numbers:
        if num < pivot:
            smaller_arr.append(num)
        if num > pivot:
            larger_arr.append(num)
        else:
            equal_arr.append(num)

    return quick_sort1(smaller_arr) + equal_arr + quick_sort1(larger_arr)

print(quick_sort1([5, 1, 4, 6, 2, 7, 5, 5, 4, 3, 6, 8, 9, 10]))

def qsort(arr):
    """배열 arr을 오름차순으로 퀵 정렬한다."""
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    low = []
    high = []
    for value in arr[1:]:
        if value < pivot:
            low.append(value)
        else:
            high.append(value)
#     print(f"{low} + {[pivot]} + {high}")
    return qsort(low) + [pivot] + qsort(high)


my_list = [24, 26, 2, 16, 32, 31, 25]
print("정렬 전:")
print(my_list)
print()
print("정렬 과정:")
print(qsort(my_list))
