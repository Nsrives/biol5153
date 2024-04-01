#! /usr/bin/env python3

def get_input():
    # get the input
    number = input('Enter the number: ')
    return number

def fibonacci(n):
    # initialize the variables for calculating the Fibonacci number at this position in the sequence
    a, b = 0, 1

    # one way to calculate the Fibonacci number
    for i in range(int(n)):
        a, b = b, a + b

    # store the result so it's obvious
    fibonacci_number = a
    return fibonacci_number

def print_number(n, fibonacci_number):
    # print the output
    print('The Fibonacci number for', n, 'is:', fibonacci_number)

def main():
    input_number = get_input()
    calculated_fibonacci = fibonacci(input_number)
    print_number(input_number, calculated_fibonacci)

# set the environment for this script
# is it main, or is this a module being called by another script
if __name__ == '__main__':
    main()
