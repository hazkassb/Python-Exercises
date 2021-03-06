# DATA COLLECTION ASSIGNMENT 2

'''
    1. Given a two list. Create a third list by picking an odd-index element from the first
    list and even index elements from second.
    Input: listOne = [3, 6, 9, 12, 15, 18, 21]      listTwo = [4, 8, 12, 16, 20, 24, 28]
    Output: [6, 12, 18, 4, 12, 20, 28]
'''


def mergeLists(list1, list2):
    res = list(list1[i] for i in range(1, len(list1), 2))

    res.extend(list2[i] for i in range(0, len(list2), 2))

    print(res)
    return


mergeLists([3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28])

'''
    2. Given a list slice it into a 3 equal chunks and reverse each list
    Input: sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    Output:
    [8, 45, 11]
    [12, 14, 23]
    [89, 45, 78]
'''


def chunck(alist):
    n = len(alist) // 3
    result = [alist[i * n:(i + 1) * n] for i in range((len(alist) + n - 1) // n)]
    result = [list(reversed(l)) for l in result]
    print(result)


chunck([11, 45, 8, 23, 14, 12, 78, 45, 89])

'''
    3. Given a list iterate it and count the occurrence of each element and create a
    dictionary to show the count of each element
    Original list [11, 45, 8, 11, 23, 45, 23, 45, 89]
    Printing count of each item {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
'''


def count_freq(alist):
    adict = dict();

    for x in alist:
        adict.update({x: alist.count(x)})

    print(adict)


count_freq([11, 45, 8, 11, 23, 45, 23, 45, 89])

'''
    4. Given two lists of equal size create a set such that it shows the element from
    both lists in the pair

    First List [2, 3, 4, 5, 6, 7, 8]
    Second List [4, 9, 16, 25, 36, 49, 64]
    Result is {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}
'''


def pairLists(list1, list2):
    res = set(zip(list1, list2))
    print(res)
    return


pairLists([2, 3, 4, 5, 6, 7, 8], [4, 9, 16, 25, 36, 49, 64])

'''
    5. Iterate a given list and Check if a given element already exists in a dictionary as
    a key’s value if not delete it from the list

    Input : rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]   
            sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
    Output: [47, 69, 76, 97]
'''


def listchecker(alist, amap):
    res = list()
    for x in alist:
        if x in amap.values():
            res.append(x)

    print(res)
    return


listchecker([47, 64, 69, 37, 76, 83, 95, 97], {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97})

'''
    6. Given a dictionary get all values from the dictionary and add it in a list but don’t add duplicates
    Input: speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
    Output: [47, 52, 44, 53, 54]
'''


def list_of_values(adict):
    res = list()
    for val in adict.values():
        if val not in res:
            res.append(val)

    print(res)
    return


list_of_values(
    {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54})

'''
    7. Remove duplicate from a list and create a tuple and find the minimum and maximum number
        Input: sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
        Output: unique items [87, 45, 41, 65, 94, 99]
        tuple (87, 45, 41, 65, 99)
        min: 41
        max: 99
'''


def tuple_min_max(alist):
    no_dups = list(set(alist))
    print("unique elements:", no_dups)

    tuple_ = tuple(no_dups)
    print("tuple:", tuple_)

    print("Minimum number: ", min(tuple_))
    print("Maximum number: ", max(tuple_))


tuple_min_max([87, 45, 41, 65, 94, 41, 99, 94])

'''
    8. You are given a list of integers. Your task is to do the following:
        1) Replace all integers that are evenly divisible by 3 with "fizz"
        2) Replace all integers divisible by 5 with "buzz"
        3) Replace all integers divisible by both 3 and 5 with "fizzbuzz"

        Input: numbers = [45, 22, 14, 65, 97, 72]
'''


def fizzbuzz(alist):
    for i in range(len(alist)):
        if alist[i] % 3 == 0 and alist[i] % 5 == 0:
            alist.__setitem__(i, 'fizzbuzz')
            continue
        elif alist[i] % 3 == 0:
            alist.__setitem__(i, 'fizz')
            continue
        elif alist[i] % 5 == 0:
            alist.__setitem__(i, 'buzz')
        else:
            continue
    print(alist)
    return


fizzbuzz([45, 22, 14, 65, 97, 72])

'''
    9. Sort the following list of complex data type in ascending order of age of an animal.
    Input: animals = [ {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5} ]
'''


def sort_(alist):
    alist = sorted(alist, key=lambda e: e['age'])

    print(alist)
    return


# sort_([{'type': 'penguin', 'name': 'Stephanie', 'age': 8},
#        {'type': 'elephant', 'name': 'Devon', 'age': 3},
#        {'type': 'puma', 'name': 'Moe', 'age': 5}])


'''
    10. You have a function named get_random_word(). It will always return a random
    selection from a small set of words:
        import random
        all_words = "all the words in the world".split()
        def get_random_word():
        return random.choice(all_words)
    Write a function get_unique_words() which repeatedly calls get_random_word() to get
    1000 random words and then return a data structure containing every unique word.
'''

import random

all_words = "all the words in the world".split()


def get_random_word():
    return random.choice(all_words)


def get_unique_words():
    unique_words = set()

    for i in range(1000):
        unique_words.add(get_random_word())

    print(unique_words)
    return


get_unique_words()

'''
    11. Given a dictionary cowboy:
    cowboy = {'age': 32, 'horse': 'mustang', 'hat_size': 'large'}
    Write a code to get the 'name' of cowboy. If key is absent, set cowboy['name'] to 'The
    Man with No Name' and return the new value.
'''


def name_cowboy(dict_cowboy):
    name = dict_cowboy.get('name', 'The Man with No Name')
    print(name)
    return


# name_cowboy({'age': 32, 'horse': 'mustang', 'hat_size': 'large'})


'''
    12. Write a program that reads integers from the user and stores them in a list. Your
    program should continue reading values until the user enters 0. Then it should display
    all of the values entered by the user (except for the 0) in order from smallest to largest,
    with one value appearing on each line. Use either the sort method or the sorted function
    to sort the list.
'''


def read_and_display():
    alist = list()

    while True:
        x = input("Enter an integer: ")
        if x == '0':
            break

        alist.append(int(x))

    alist.sort()

    for val in alist:
        print(val)


# read_and_display()


'''
    13. Create a program that reads integers from the user until a blank line is entered.
    Once all of the integers have been read your program should display all of the negative
    numbers, followed by all of the zeros, followed by all of the positive numbers. Within
    each group the numbers should be displayed in the same order that they were entered
    by the user. For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then your
    program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program should display
    each value on its own line.
'''


def reader():
    pos, zeros, negs = list(), list(), list()

    while True:
        x = input("Enter an integer: ")
        if x == "":
            break

        if int(x) < 0:
            negs.append((int(x)))
            continue
        if int(x) == 0:
            zeros.append((int(x)))
            continue
        if int(x) > 0:
            pos.append(int(x))

    for x in negs:
        print(x)
    for x in zeros:
        print(x)
    for x in pos:
        print(x)

    return


reader()