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
# Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.

# Ans
# Trailing 0s in n! = Count of 5s in prime factors of n!

import math 

def zeros(n):
    if n < 0:
        return -1
    i=5
    result = 0
    while n/i >= 1:
    # for i in range(i, n/i >= 1, i):
        result += n//i   #   = (n/5) + (n/25) + (n/125) + ....
        i*=5

    return result

# Others OK answers
def zeros_1(n):
  x = n/5
  return x+zeros_1(x) if x else 0

def zeros_2(n):
    res = 0
    while n >= 5:
        res += n // 5
        n //= 5
    
    return res
 
def zeros_3(n):
  if (n >= 5):
      return math.floor(n / 5) + zeros_3(n / 5)
  else:
      return 0

import itertools

def zeros_4(n):
    powers_of_5 = itertools.takewhile(lambda x: n/x > 0, (5**x for x in itertools.count(1)))

    return sum(n / x for x in powers_of_5)

# Performance NG
# def zeros_old(n):
#     result = 0
#     for i in range(t,n+1,t):
#         while i>=t:
#             if i%t==0:
#                 i=i//t
#                 result+=1
#             else:
#                 break
#     return result


# Performance NG
# def zeros(n):
#     multiply_result = math.factorial(n)
#     multiply_str = str(multiply_result)
#     result = len(multiply_str) - len(multiply_str.rstrip('0'))
#     return result



if __name__ == "__main__":
    # print(zeros(0)) #0
    # print(zeros(4)) #0
    # print(zeros(5)) #1
    # print(zeros(9)) #1
    # print(zeros(10)) #2
    # print(zeros(15)) #3
    # print(zeros(19)) #3
    # print(zeros(75)) #18
    # print(zeros(100)) #24
    # print(zeros_3(245)) #48
    # print(zeros_3(1000)) #249
    # print(zeros(10000))  #2499
    # print(zeros(100000))  #24999
    # print(zeros(50000))  #12499
    # print(zeros(1000000)) 
    # print(zeros(1000000000)) #249999998



