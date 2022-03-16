# Define a function that takes one integer argument 
# and returns logical value true or false depending 
# on if the integer is a prime.

# Per Wikipedia, a prime number (or a prime) is a natural 
# number greater than 1 that has no positive divisors other 
# than 1 and itself.

# Importance to consider performance for big numbers
import math


def is_prime(num):
    if num < 2:
        return False
    digits = int(math.log10(num))+1
    range_num = num
    if digits > 2:
        range_num = int(math.sqrt(num)) + 1

    results = set(False if num%i == 0 else True for i in range(2, range_num))
    return not False in results

from math import sqrt

def is_prime_2(num):
    if num <= 1:
        return False
    i = 2
    while i <= sqrt(num):    
        if num%i == 0:
            return False
        i += 1
    return True 

if __name__ == "__main__":
    print(is_prime(34421689)) # False
    print(is_prime(39677401)) # False
    print(is_prime(910168561)) # False
    print(is_prime(21003889)) # False
    print(is_prime(188265841)) # False
    print(is_prime(4))  # False
    print(is_prime(1853606873)) # True
    print(is_prime(5099)) # True
    print(is_prime(0)) # False
    print(is_prime(1)) # False
    print(is_prime(2)) # True
    print(is_prime(13)) # True
    print(is_prime(-2)) # False
    print(is_prime(6)) # False
    
