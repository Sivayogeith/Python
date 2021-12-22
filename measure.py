import math
import htol
import ltoh



num1 = int(input("\nPlease Enter The First Num:"))

num2 = int(input("\nPlease Enter The Second Num:"))

unit1 = input("\nPlease Enter The First Unit:")

unit2 = input("\nPlease Enter The Second Unit:")

unit1_checker = unit1[0]
da_checker = unit1[0] + unit1[1]

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


    print("\nAnswer is:", ltoh.lh() , unit2)
else :
    print('Something went wrong Try Again!')