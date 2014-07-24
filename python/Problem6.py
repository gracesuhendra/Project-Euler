'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of
the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of
the first one hundred natural numbers and the square of the sum.
'''

def sum_squares(n):
    total = 0
    for i in range(1, n+1):
        total = total + i*i
    return total

def square_sum(n):
    total = 0
    for i in range(1, n+1):
        total = total + i
    return total*total

def diff(n):
    return square_sum(n) - sum_squares(n)

print diff(100)
