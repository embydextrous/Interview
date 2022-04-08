'''
Every positive fraction can be represented as sum of unique unit fractions. 
A fraction is unit fraction if numerator is 1 and denominator is a positive integer, 
for example 1/3 is a unit fraction. 
Such a representation is called Egyptian Fraction as it was used by ancient Egyptians. 
Following are few examples: 
 
Egyptian Fraction Representation of 2/3 is 1/2 + 1/6
Egyptian Fraction Representation of 6/14 is 1/3 + 1/11 + 1/231
Egyptian Fraction Representation of 12/13 is 1/2 + 1/3 + 1/12 + 1/156
'''
import math

def egyptianFraction(n, d):
    print("The egyptian fractions for {}/{} are:".format(n, d), end = " ")
    result = []
    while n != 0:
        x = math.ceil(d/n)
        n = n * x - d
        d *= x
        result.append(x)
    for i in result:
        print("1/{}".format(i), end = " ")
    print()

egyptianFraction(79, 87)