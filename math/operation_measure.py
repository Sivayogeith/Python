from decimal import *
from os import system
getcontext().prec = 6

num1 = input("\nPlease Enter The First Number:")

num2 = input("\nPlease Enter The Second Number:")

operations = input("\nPlease Enter The Operation:")

def operation():
    ans = ''
    if operations == "add":
        ans = Decimal(num1) + Decimal(num2)
    elif operations == "sub":
        ans = Decimal(num1) - Decimal(num2)
    elif operations == "mul":
        ans = Decimal(num1) * Decimal(num2)
    elif operations == "div":
        ans = Decimal(num1) / Decimal(num2)
    else:
        _ = system("clear")
        print("\nPlease Use add/sub/mul/div")
        
        

    return ans

print("\nAnswer:", operation())