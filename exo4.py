'''1. Write a Python program that accepts a word from the user and reverse it. Hint: Use built-in function input()'''
def reverse():
    user_input = input("Enter a word: ")
    print(user_input[-1 : : -1])

# reverse()


'''2. Write a Python program that counts the number of even and odd numbers from a series of numbers.
            I/P: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
            O/P: Number of even numbers: 4 Number of odd numbers: 5
'''
def countEvenOdd():
    user_input = input("Please enter a stream of comma separated numbers: ")
    count_even = 0

    for num in user_input.split(","):
        if int(num)%2 == 0:
            count_even += 1

    print("Number of even numbers: {} \n Number of odd numbers: {}".format(count_even, len(user_input.split(","))-count_even))

# countEvenOdd()


'''3. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. Node: Use 'continue' statement.'''
def print_():
    for num in range(7):
        if num == 3 or num == 6:
            continue
        print(num)

# print_()


'''4. Write a Python program to check whether an alphabet is a vowel or consonant
            I/P: Input a letter of the alphabet k.
            O/P: k is a consonant.
'''
def checkAlphabet():
    vowels = "aeiou"
    user_input = input("Enter a letter of the alphabet: ")

    if user_input in vowels:
        print("{} is a vowel.".format(user_input))
    else:
        print("{} is a consonant.".format(user_input))

# checkAlphabet()

