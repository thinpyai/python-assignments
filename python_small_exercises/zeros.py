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
from unittest import result


def zeros(n):
    count_5 = count(n,5)
    return count_5

def count(n,t):
    result = 0
    for i in range(t,n+1,t):
        while i>=t:
            if i%t==0:
                i=i//t
                result+=1
            else:
                break
    return result

def multiply(n):
    result = 1
    for i in range(1,n+1):
        result=result*i
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

    print(multiply(1000000))
    print(zeros(1000000)) 
    
    # print(multiply(1000000000))
    # print(zeros(1000000000))  #24999