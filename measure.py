import math
import htol
import ltoh
import base_unit
from os import system

try :
    num1 = int(input("\nPlease Enter The First Num:"))

    num2 = int(input("\nPlease Enter The Second Num:"))

    unit1 = input("\nPlease Enter The First Unit:")

    unit2 = input("\nPlease Enter The Second Unit:")

except KeyboardInterrupt:
    error = input("\nWant to Give Up Now? Y/N\n")
    if error == "Y" and error == "y":
        _ = system('clear')
        print("You Gave Up!")
        exit()
    elif error == "N" and error == "n":
        _ = system('clear')
        f = open('measure.py', 'r')
        temp = f.read()
        f.close()

        code = compile(temp, 'measure.py', 'exec')
        exec(code)

unit1_checker = unit1[0]
def da_checker():
    if unit1_checker == "d":
        da_checker = unit1[0] + unit1[1]
    return da_checker

if unit1_checker == "k" or unit1_checker == "h" or da_checker == "da":

    htol.num1 = num1
    htol.num2 = num2
    htol.unit1 = unit1
    htol.unit2 = unit2


    print("\nAnswer is:", htol.hl() , unit2)
elif unit1_checker == "m" or unit1_checker == "c" or unit1_checker == "d":
    
    ltoh.num1 = num1
    ltoh.num2 = num2
    ltoh.unit1 = unit1
    ltoh.unit2 = unit2

elif unit1_checker == "l" or unit1_checker == "g" or unit1_checker == "m":
    
    base_unit.num1 = num1
    base_unit.num2 = num2
    base_unit.unit1 = unit1
    base_unit.unit2 = unit2


    print("\nAnswer is:", base_unit.bu() , unit2)
else :
    print('Something went wrong Try Again!')