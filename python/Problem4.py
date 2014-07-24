'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def palin():
    nums = []
    i = 100
    while (i<1000):
        j = 100
        while (j<1000):
            num = i * j
            if str(num)[::-1] == str(num):
                nums.append(num)
            j = j+1
        i = i+1
    return max(nums)

print palin() 
