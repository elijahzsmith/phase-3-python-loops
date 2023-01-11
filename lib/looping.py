#!/usr/bin/env python3

def happy_new_year():
    # code goes here
    i = 10
    while i > 0:
        print(i)
        i = i - 1

    print("Happy New Year!")
    
    

def square_integers(int_list):
    # code goes here
    return [int * int for int in int_list]

def fizzbuzz():
    # code goes here
    for i in range(100):
        current = i + 1
        if current % 3 == 0 and current % 5 == 0:
            print("FizzBuzz")
        elif current % 3 == 0:
            print("Fizz")
        elif current % 5 == 0:
            print("Buzz")
        else:
            print(current)



