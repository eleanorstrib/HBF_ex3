"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calc():
    while True:
        user_input = raw_input(">")
        listy = user_input.split(" ")
        operation = listy[0]
        num1 = int(listy[1])
        num2 = int(listy[2])

        if operation == 'q':
            break

        if operation == "+":
            add(num1,num2)



def main():
	# Your code goes here
	calc()


if __name__ == '__main__':
    main()
