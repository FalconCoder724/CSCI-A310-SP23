#Sai Mullangi
#Homework 3

#Question 1
(a, b) = (2.1, 2.9)

assert(round( a), round( b)) == (2,3), "Test 01.a failed" 
assert(round(-a), round(-b)) == (-2,-3), "Test 01.b failed" 

print('Q1 is All good!')

#Question 2

assert(int( a), int( b)) == (2,2), "Test 02.a failed" 
assert(int(-a), int(-b)) == (-2,-2), "Test 02.b failed" 

print('Q2 is All good!')

#Question 3
assert(list(range(12, 16)) == [12,13,14,15]), "Test 03.a failed"
assert(list(range(0, 10, 2)) == [0,2,4,6,8]), "Test 03.b failed"
assert(list(range(5, -1, -1)) == [5,4,3,2,1,0]), "Test 03.c failed"

print('Q3 is All good!')

#Question 4
import random
assert 1 <= random.randint(1,10) <= 10, "Test 04.a failed"
assert random.randint(1,2) in [1,2], "Test 04.b failed"

print('Q4 is All good!')

#Question 5
#Given
def what(n): # n > 0
    if n == 1: return 1
    else: return(n) + what(n - 1)

assert(what(10) == 55), "Test 05 failed"
print('Q5 is All good!')

#Question 6
#Given
def what(n, m):
    if n < 0:
        return -what(-n, m)
    else:
        if n == 1:
            return m
        else:
            return m + what(n-1, m)

assert(what(-5,3) == -15), 'Test 06 failed'
print('Q6 is All good!')

#Question 7
#Given
def what():
  pass

assert(what() == None), "Test 07 failed"

print('Q7 is All good!')

#Question 8
#Given
a = [3, 1, 5, 6, 4, 2] 
random.choice(a)

assert(random.choice(a) in [1, 2, 3, 4, 5, 6]), "Test 08 failed"
print('Q8 is All good!')

#Question 9
b = sorted(a)
random.shuffle(a)
assert(sorted(a) == b), "Test 09 failed"

print('Q9 is All good!')

#Question 10
#Given
try:
  print(1 + 'a') #Won't work b/c python won't allow the concatination of strings and integers, need to have 1 converted to a string using the str() function
except:
  print('1a'); # This works because 1 and a are together and classified as a string in the print function as they are in quotes together.
#Test 10 would print 1a
print('Test 10 would print 1a')

#Prints all tests are passed
print("All tests are passed")

#Question 11
#Given from Book

numberOfStreaks = 0
#print("test")
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    #print("test")
    coins = []
    #print("Test")
    for i in range(100):
        #print('if loop test')
        if random.randint(0,1) == 0:
            coins += 'H'
        else: 
            coins += 'T'
        coins = ''.join(coins)
    # Code that checks if there is a streak of 6 heads or tails in a row.
    if "H" * 6 in coins or "T" * 6 in coins:
        numberOfStreaks += 1
print('Chance of streak: %s%%' % (numberOfStreaks / 100)) #  ~80.3%

#Question 12
matrix = {}
value = 1
for row in range(3):
    for col in range(3):
        matrix[row,col] = value
        value += 1
print(matrix)

#Question 13
print('Sai\'s question 11 is taking too long to run.')
print(r'That is Sai\'s work.')
print('''Dear Dr. German,
I have tried multiple types of code for question 11 and even your examples but mine running forever why is it doing so?
Sincerely,
Sai''')
"""This is a mutli line comment
stating that I used it in Question 11 so I can test all my other code.
"""

#Question 14
print("Iamtired".isalpha()) #print true
print('I am tried'.isspace()) #print false
print('Python'.istitle()) #print true

print(', '.join(['cats', 'rats', 'bats'])) #'cats, rats, bats'
print(' '.join(['My', 'name', 'is', 'Simon'])) #'My name is Simon'
print('ABC'.join(['My', 'name', 'is', 'Simon'])) #'MyABCnameABCisABCSimon'

print('My name is Simon'.split()) #['My', 'name', 'is', 'Simon']
print('MyABCnameABCisABCSimon'.split('ABC')) #['My', 'name', 'is', 'Simon']
print('My name is Simon'.split('m')) #['My na', 'e is Si', 'on']

#Question 15
print('Hello'.rjust(20))#             Hello
print('Hello'.center(20, '='))#'=======Hello========'

tester = '     Monty Python     '
print(tester.strip())#Monty Python

print(ord('B')) #65
print(chr(65)) #A