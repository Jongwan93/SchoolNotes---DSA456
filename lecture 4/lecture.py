# any string that contains two upper case, turn the entire string into uppercase
from collections import Counter


def toUpperString(message):
    count = 0

    for ch in message:
        if ch.isupper():
            count+=1
            if count >= 2:
                return message.upper()

print(toUpperString("Hello World")) # HELLO WORLD

print()
print("========================================================================================")
#=======================================================================================================
print()

def remove_duplicates(fruits):
    # for i in range(0, len(fruits)):
        # for j in range(i+1, len(fruits)):
            # if(fruits[i] == fruits[j]):
                # fruits[j] = ''

    # return fruits

    # result = []
    # for fruit in fruits:
        # if fruit not in result:
            # result.append(fruit)
    # return result

    # set is data structure like array, that cannot hold duplicates
    # difference between list and set is set CANNOT hold duplicate values
    # however, set will shuffle the order of data. 
    # therefore, do not use it if you need it sorted
    return list(set(fruits))

print(remove_duplicates(['Apple', 'Orange', 'Apple', 'Banana', 'Orange']))


print()
print("========================================================================================")
#=======================================================================================================
print()

def is_common(first, second):
    for i in first:
        if i in second:
            return True
    return False

print(is_common([1, 2, 3, 4, 5], [5, 6, 7, 8]))

print()
print("========================================================================================")
#=======================================================================================================
print()

def second_smallestnumbers(numbers):
    numbers.sort()
    return numbers[1]

    return sorted(numbers)[1]

print(second_smallestnumbers([1, 5, 2, 3, 4]))

print()
print("========================================================================================")
#=======================================================================================================
print()

def split_list(list, n):
    count = 0
    while(count > 0):
        return

print(split_list([1, 2, 3, 4, 5, 6, 7, 8], 2))

print()
print("========================================================================================")
#=======================================================================================================
print()

def iterate_lists(fruits, freqs):
    # zip function will iterate these two arrays in same index
    for fruit, freq in zip(fruits, freqs): # fruits[0] freqs[0]
        # fruit = fruits, freq = freqs
        print("{}: {}".format(fruit, freq))

iterate_lists(['Apple', 'Banana', 'Orange'], [3, 2, 1]) # {'Apple' : 3, 'Banana': 2, 'Orange' : 1}

print()
print("========================================================================================")
#=======================================================================================================
print()

def get_frequencies(fruits):
    # frequencies = []
    # for fruit in fruits:
    #  found = False
    #   for i in range(len(frequencies)):
    #        if frequencies[i][0] == fruits:
    #            frequencies[i][1] += 1
    
    # freqs = {}
    # for fruit in fruits:
    # if fruit in freqs.keys():
    #    freqs[fruit] += 1 # freqs['Apple'] increased by 1
    # else:
    #      freqs[fruit] = 1 # freqs['Apple'] = 1
    # return freqs

    return dict(Counter(fruits))

print(get_frequencies(['Apple', 'Orange', 'Banana', 'Apple', 'Orange', 'Apple'])) # Apple : 3, Orange : 2, Bananad : 1