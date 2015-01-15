"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

mathness = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide, 
    'square': square, 
    'cube': cube, 
    'pow': power,
    'mod': mod
}

def calc():
    while True:
        user_input = raw_input(">")
        listy = user_input.split(" ")
        operation = listy[0]
        if operation == 'q':
            break

        elif operation in mathness:
            num1 = int(listy[1])
            num2 = int(listy[2])
            for key in mathness:
                if key == operation:
                    mathness[operation]
                    funk = mathness.get(key)
                    answer=funk(num1, num2)
                    print answer  

        else:
            print "I don't understand"
        

def main():
	# Your code goes here
	calc()


if __name__ == '__main__':
    main()
