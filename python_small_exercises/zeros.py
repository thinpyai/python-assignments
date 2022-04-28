# Number of trailing zeros of N!

# Write a program that will calculate the number of trailing zeros in a factorial of a given number.

# N! = 1 * 2 * 3 * ... * N

# Be careful 1000! has 2568 digits...

# For more info, see: http://mathworld.wolfram.com/Factorial.html

# Examples
# zeros(6) = 1
# # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

# zeros(12) = 2
# # 12! = 479001600 --> 2 trailing zeros

# 1000000000 must be finished within 12000 ms
from ast import operator
from unittest import result


def zeros(n):
    count_5 = count_1(n,5)
    return count_5

# For is slower than while
def count_1(n,t):
    result = 0
    for i in range(t,n+1,t):
        while i>=t:
            if i%t==0:
                i=i//t
                result+=1
            else:
                break
    return result

# Performance NG
def count_2(n,t):
    result = 0
    i = t
    while i in range(t,n+1):
        j=i
        while j>=t:
            if j%t==0:
                j=j//t
                result+=1
            else:
                break
        i+=t
    return result

# --------------    

def multiply_1(n):
    result = 1
    i = 2
    for i in range(2,n+1):
        result=result*i
    return result


def multiply_2(n):
    result = 1
    i = 2
    while i in range(2,n+1):
        result*=i
        i+=1
    return result

# -------------- 

import math

def zeros(n):
    multiply_result = math.factorial(n)
    multiply_str = str(multiply_result)
    result = len(multiply_str) - len(multiply_str.rstrip('0'))
    return result


if __name__ == "__main__":
    # print(zeros(0)) #0

    # print(multiply(5)) 
    # print(zeros(5)) #1

    # print(multiply(10))
    # print(zeros(10)) #2

    # print(multiply(15))
    # print(zeros(15)) #3
    
    # print(multiply(6))
    # print(zeros(6)) #1

    # print(multiply(12))
    # print(zeros(12)) #2

    # print(multiply(18))
    # print(zeros(18)) #3

    # print(multiply(30))
    # print(zeros(30)) #7

    # print(multiply(1000))
    # print(zeros(1000)) #249

    # print(multiply(10000))
    # print(zeros(10000))  #2499

    # print(multiply(100000))
    # print(zeros(100000))  #24999

    # print(multiply(50000))
    # print(zeros(50000))  #12499

    # print(multiply(1000000))
    print(zeros(1000000)) 
    
    # print(multiply(1000000000))
    # print(zeros(1000000000))  #24999