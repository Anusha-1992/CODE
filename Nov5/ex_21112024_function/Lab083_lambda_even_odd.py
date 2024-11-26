# writte prog to find the EVEN number or ODD
import math


def find_even_odd(num):
    if num % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

find_even_odd(18)

# by using lambda and ternary

even_odd = lambda num : "EVEN " if num % 2==0  else "ODD"
print(even_odd(15))
print(even_odd(10))
print(even_odd(15))
print(even_odd(2))

op2 = lambda :math.pow(int(input("Enter the number: \n")),6)
print(op2())
