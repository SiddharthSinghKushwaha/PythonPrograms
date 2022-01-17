# Write a program to use some common math module function like min, max, floor, gcd, factorial, sqrt and so on.
import math
# Constants provided by the math module

# Euler’s Number
print(math.e)

# Pi
print(math.pi)

# Tau: Tau is defined as the ratio of the circumference to the radius of a circle.
print(math.tau)

# Infinity
print(math.inf)     # Print the positive infinity
print(-math.inf)    # Print the negative infinity

# Not a Number (NaN)
# The math.nan constant returns a floating-point nan (Not a Number) value. This value is not a legal number.
print(math.nan)

# Numeric Functions
# ceil() and floor()
a = 2.3
print("The ceil of 2.3 is : ", math.ceil(a))
print("The floor of 2.3 is : ", math.floor(a))

# factorial()
print('The factorial of a number:', math.factorial(5))

# gcd() function is used to find the greatest common divisor of two numbers passed as the arguments.
print('The GCD of 64 nad 12 is ', math.gcd(64, 12))

# fabs() function returns the absolute value of the number.
print('The absolute value of |-3.4| is ', math.fabs(-3.4))

# exp(), log(__, base), log2(), log10(), pow(), sqrt()
print('The exponential value of 5 is', math.exp(5))
print('The log value of 6 base 3 is ', math.log(6, 3))
print('The log2 of 32 is', math.log2(32))
print('The log10 of 1000 is', math.log10(1000))

print('2 to power 4 is', math.pow(2, 4))
print('Square root of 64 is', math.sqrt(64))

# isinf(), isnan(), sin(), cos(), tan(),
print('Check for Infinity number', math.isinf(float('inf')))
print('Check for Not a Number number', math.isinf(float('nan')))

# degrees() function is used to convert argument value from radians to degrees.
print(math.degrees(30))

# radians() function is used to convert argument value from degrees to radians.
print(math.radians(45))
