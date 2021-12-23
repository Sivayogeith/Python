unit1 = ''
unit2 = ''
num1 = ''
num2 = ''

def bu():
    
    # |*****************************************|
    #  Higher Units to Lower Units
    # |*****************************************|

    # ----------------- Length -----------------

    if unit1 == "km" and unit2 == "hm":
        ans = int(num1) * 10 + int(num2)
    if unit1 == "km" and unit2 == "dam":
        ans = int(num1) * 100 + int(num2)
    if unit1 == "km" and unit2 == "m":
        ans = int(num1) * 1000 + int(num2)
    if unit1 == "km" and unit2 == "dm":
        ans = int(num1) * 10000 + int(num2)
    if unit1 == "km" and unit2 == "cm":
        ans = int(num1) * 100000 + int(num2)
    if unit1 == "km" and unit2 == "mm":
        ans = int(num1) * 1000000 + int(num2)

    if unit1 == "hm" and unit2 == "dam":
        ans = int(num1) * 10 + int(num2)
    if unit1 == "hm" and unit2 == "m":
        ans = int(num1) * 100 + int(num2)
    if unit1 == "hm" and unit2 == "dm":
        ans = int(num1) * 1000 + int(num2)
    if unit1 == "hm" and unit2 == "cm":
        ans = int(num1) * 10000 + int(num2)
    if unit1 == "hm" and unit2 == "mm":
        ans = int(num1) * 100000 + int(num2)

    if unit1 == "dam" and unit2 == "m":
        ans = int(num1) * 10 + int(num2)
    if unit1 == "dam" and unit2 == "dm":
        ans = int(num1) * 100 + int(num2)
    if unit1 == "dam" and unit2 == "cm":
        ans = int(num1) * 1000 + int(num2)
    if unit1 == "dam" and unit2 == "mm":
        ans = int(num1) * 10000 + int(num2)

    if unit1 == "m" and unit2 == "dm":
        ans = int(num1) * 10 + int(num2)
    if unit1 == "m" and unit2 == "cm":
        ans = int(num1) * 100 + int(num2)
    if unit1 == "m" and unit2 == "mm":
        ans = int(num1) * 1000 + int(num2)
    if unit1 == "m" and unit2 == "m":
        ans = int(num1) * 0 + int(num2)

    if unit1 == "dm" and unit2 == "cm":
        ans = int(num1) * 100 + int(num2)
    if unit1 == "dm" and unit2 == "mm":
        ans = int(num1) * 1000 + int(num2)

    if unit1 == "cm" and unit2 == "mm":
        ans = int(num1) * 1000 + int(num2)


    #  ----------------- Mass -----------------

    if unit1 == "kg" and unit2 == "hg":
        ans = int(num1) * 10 + int(num2)
    if unit1 == "kg" and unit2 == "dag":
        ans = int(num1) * 100 + int(num2)
    if unit1 == "kg" and unit2 == "g":
        ans = int(num1) * 1000 + int(num2)
    if unit1 == "kg" and unit2 == "dg":
        ans = int(num1) * 10000 + int(num2)
    if unit1 == "kg" and unit2 == "cg":
        ans = int(num1) * 100000 + int(num2)
    if unit1 == "kg" and unit2 == "mg":
        ans = int(num1) * 1000000 + int(num2)

    if unit1 == "hg" and unit2 == "dag":
        ans = int(num1) * 10 + int(num2)
    if unit1 == "hg" and unit2 == "v":
        ans = int(num1) * 100 + int(num2)
    if unit1 == "hg" and unit2 == "dg":
        ans = int(num1) * 1000 + int(num2)
    if unit1 == "hg" and unit2 == "cg":
        ans = int(num1) * 10000 + int(num2)
    if unit1 == "hg" and unit2 == "mg":
        ans = int(num1) * 100000 + int(num2)


    if unit1 == "dag" and unit2 == "g":
        ans = int(num1) * 10 + int(num2)
    if unit1 == "dag" and unit2 == "dg":
        ans = int(num1) * 100 + int(num2)
    if unit1 == "dag" and unit2 == "cg":
        ans = int(num1) * 1000 + int(num2)
    if unit1 == "dag" and unit2 == "mg":
        ans = int(num1) * 10000 + int(num2)

    if unit1 == "g" and unit2 == "dg":
        ans = int(num1) * 10 + int(num2)
    if unit1 == "g" and unit2 == "cg":
        ans = int(num1) * 100 + int(num2)   
    if unit1 == "g" and unit2 == "mg":
        ans = int(num1) * 1000 + int(num2)
    if unit1 == "g" and unit2 == "g":
        ans = int(num1) * 0 + int(num2)

    if unit1 == "dg" and unit2 == "cg":
        ans = int(num1) * 100 + int(num2)
    if unit1 == "dg" and unit2 == "mg":
        ans = int(num1) * 1000 + int(num2)

    if unit1 == "cg" and unit2 == "mg":
        ans = int(num1) * 1000 + int(num2)

    # ----------------- Capacity -----------------

    if unit1 == "kl" and unit2 == "hl":
        ans = int(num1) * 10 + int(num2)
    if unit1 == "kl" and unit2 == "dal":
        ans = int(num1) * 100 + int(num2)
    if unit1 == "kl" and unit2 == "l":
        ans = int(num1) * 1000 + int(num2)
    if unit1 == "kl" and unit2 == "dl":
        ans = int(num1) * 10000 + int(num2)
    if unit1 == "kl" and unit2 == "cl":
        ans = int(num1) * 100000 + int(num2)
    if unit1 == "kl" and unit2 == "ml":
        ans = int(num1) * 1000000 + int(num2)
    
    if unit1 == "hl" and unit2 == "dal":
        ans = int(num1) * 10 + int(num2)
    if unit1 == "hl" and unit2 == "l":
        ans = int(num1) * 100 + int(num2)
    if unit1 == "hl" and unit2 == "dl":
        ans = int(num1) * 1000 + int(num2)
    if unit1 == "hl" and unit2 == "cl":
        ans = int(num1) * 10000 + int(num2)
    if unit1 == "hl" and unit2 == "ml":
        ans = int(num1) * 100000 + int(num2)

    if unit1 == "dal" and unit2 == "l":
        ans = int(num1) * 10 + int(num2)
    if unit1 == "dal" and unit2 == "dl":
        ans = int(num1) * 100 + int(num2)
    if unit1 == "dal" and unit2 == "cl":
        ans = int(num1) * 1000 + int(num2)
    if unit1 == "dal" and unit2 == "ml":
        ans = int(num1) * 10000 + int(num2)

    if unit1 == "l" and unit2 == "dl":
        ans = int(num1) * 10 + int(num2)
    if unit1 == "l" and unit2 == "cl":
        ans = int(num1) * 100 + int(num2) 
    if unit1 == "l" and unit2 == "ml":
        ans = int(num1) * 1000 + int(num2)
    if unit1 == "l" and unit2 == "l":
        ans = int(num1) * 0 + int(num2)
    
    if unit1 == "dl" and unit2 == "cl":
        ans = int(num1) * 100 + int(num2)
    if unit1 == "dl" and unit2 == "ml":
        ans = int(num1) * 1000 + int(num2)

    if unit1 == "cl" and unit2 == "ml":
        ans = int(num1) * 1000 + int(num2)

    # |*****************************************|
    #  Lower Units to Higher Units
    # |*****************************************|

    # ----------------- Length -----------------

    if unit1 == "mm" and unit2 == "km":
        ans = int(num1) / 1000000 + int(num2)
    if unit1 == "mm" and unit2 == "hm":
        ans = int(num1) / 100000 + int(num2)
    if unit1 == "mm" and unit2 == "dam":
        ans = int(num1) / 10000 + int(num2)
    if unit1 == "mm" and unit2 == "m":
        ans = int(num1) / 1000 + int(num2)
    if unit1 == "mm" and unit2 == "dm":
        ans = int(num1) / 100 + int(num2)
    if unit1 == "mm" and unit2 == "cm":
        ans = int(num1) / 10 + int(num2)

    if unit1 == "cm" and unit2 == "km":
        ans = int(num1) / 100000 + int(num2)
    if unit1 == "cm" and unit2 == "hm":
        ans = int(num1) / 10000 + int(num2)
    if unit1 == "cm" and unit2 == "dam":
        ans = int(num1) / 1000 + int(num2)
    if unit1 == "cm" and unit2 == "m":
        ans = int(num1) / 100 + int(num2)
    if unit1 == "cm" and unit2 == "dm":
        ans = int(num1) / 10 + int(num2)

    if unit1 == "dm" and unit2 == "km":
        ans = int(num1) / 10000 + int(num2)
    if unit1 == "dm" and unit2 == "hm":
        ans = int(num1) / 1000 + int(num2)
    if unit1 == "dm" and unit2 == "dam":
        ans = int(num1) / 100 + int(num2)
    if unit1 == "dm" and unit2 == "m":
        ans = int(num1) / 10 + int(num2)

    if unit1 == "m" and unit2 == "km":
        ans = int(num1) / 1000 + int(num2)
    if unit1 == "m" and unit2 == "hm":
        ans = int(num1) / 100 + int(num2)
    if unit1 == "m" and unit2 == "dam":
        ans = int(num1) / 10 + int(num2)
    if unit1 == "m" and unit2 == "m":
        ans = int(num1) / 0 + int(num2)
    
    if unit1 == "dam" and unit2 == "km":
        ans = int(num1) / 100 + int(num2)
    if unit1 == "dam" and unit2 == "hm":
        ans = int(num1) / 10 + int(num2)
    
    if unit1 == "hm" and unit2 == "km":
        ans = int(num1) / 10 + int(num2)

    #  ----------------- Mass -----------------

    if unit1 == "mg" and unit2 == "kg":
        ans = int(num1) / 1000000 + int(num2)
    if unit1 == "mg" and unit2 == "hg":
        ans = int(num1) / 100000 + int(num2)
    if unit1 == "mg" and unit2 == "dag":
        ans = int(num1) / 10000 + int(num2)
    if unit1 == "mg" and unit2 == "g":
        ans = int(num1) / 1000 + int(num2)
    if unit1 == "mg" and unit2 == "dg":
        ans = int(num1) / 100 + int(num2)
    if unit1 == "mg" and unit2 == "cg":
        ans = int(num1) / 10 + int(num2)

    if unit1 == "cg" and unit2 == "kg":
        ans = int(num1) / 100000 + int(num2)
    if unit1 == "cg" and unit2 == "hg":
        ans = int(num1) / 10000 + int(num2)
    if unit1 == "cg" and unit2 == "dag":
        ans = int(num1) / 1000 + int(num2)
    if unit1 == "cg" and unit2 == "g":
        ans = int(num1) / 100 + int(num2)
    if unit1 == "cg" and unit2 == "dg":
        ans = int(num1) / 10 + int(num2)

    if unit1 == "dg" and unit2 == "kg":
        ans = int(num1) / 10000 + int(num2)
    if unit1 == "dg" and unit2 == "hg":
        ans = int(num1) / 1000 + int(num2)
    if unit1 == "dg" and unit2 == "dag":
        ans = int(num1) / 100 + int(num2)
    if unit1 == "dg" and unit2 == "g":
        ans = int(num1) / 10 + int(num2)

    if unit1 == "g" and unit2 == "kg":
        ans = int(num1) / 1000 + int(num2)
    if unit1 == "g" and unit2 == "hg":
        ans = int(num1) / 100 + int(num2)
    if unit1 == "g" and unit2 == "dag":
        ans = int(num1) / 10 + int(num2)
    if unit1 == "g" and unit2 == "g":
        ans = int(num1) / 0 + int(num2)

    if unit1 == "dag" and unit2 == "kg":
        ans = int(num1) / 100 + int(num2)
    if unit1 == "dag" and unit2 == "hg":
        ans = int(num1) / 10 + int(num2)
    
    if unit1 == "hg" and unit2 == "kg":
        ans = int(num1) / 10 + int(num2)
    # ----------------- Capacity -----------------

    if unit1 == "ml" and unit2 == "kl":
        ans = int(num1) / 1000000 + int(num2)
    if unit1 == "ml" and unit2 == "hl":
        ans = int(num1) / 100000 + int(num2)
    if unit1 == "ml" and unit2 == "dal":
        ans = int(num1) / 10000 + int(num2)
    if unit1 == "ml" and unit2 == "l":
        ans = int(num1) / 1000 + int(num2)
    if unit1 == "ml" and unit2 == "dl":
        ans = int(num1) / 100 + int(num2)
    if unit1 == "ml" and unit2 == "cl":
        ans = int(num1) / 10 + int(num2)

    if unit1 == "cl" and unit2 == "kl":
        ans = int(num1) / 100000 + int(num2)
    if unit1 == "cl" and unit2 == "hl":
        ans = int(num1) / 10000 + int(num2)
    if unit1 == "cl" and unit2 == "dal":
        ans = int(num1) / 1000 + int(num2)
    if unit1 == "cl" and unit2 == "l":
        ans = int(num1) / 100 + int(num2)
    if unit1 == "cl" and unit2 == "dl":
        ans = int(num1) / 10 + int(num2)

    if unit1 == "dl" and unit2 == "kl":
        ans = int(num1) / 10000 + int(num2)
    if unit1 == "dl" and unit2 == "hl":
        ans = int(num1) / 1000 + int(num2)
    if unit1 == "dl" and unit2 == "dal":
        ans = int(num1) / 100 + int(num2)
    if unit1 == "dl" and unit2 == "l":
        ans = int(num1) / 10 + int(num2)


    if unit1 == "l" and unit2 == "kl":
        ans = int(num1) / 1000 + int(num2)
    if unit1 == "l" and unit2 == "hl":
        ans = int(num1) / 100 + int(num2)
    if unit1 == "l" and unit2 == "dal":
        ans = int(num1) / 10 + int(num2)
    if unit1 == "l" and unit2 == "l":
        ans = int(num1) / 0 + int(num2)
    
    if unit1 == "dal" and unit2 == "kl":
        ans = int(num1) / 100 + int(num2)
    if unit1 == "dal" and unit2 == "hl":
        ans = int(num1) / 10 + int(num2)
    
    if unit1 == "hl" and unit2 == "kl":
        ans = int(num1) / 10 + int(num2)
    return ans