def roman_to_integer(rom):
    roman = {
        'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000
    }

    total = 0 

    for i in range(len(rom)):
        current = roman[rom[i]]

        if i+1 < len(rom) and roman[rom[i]] < roman[rom[i+1]]:
            total-=current
        else:
            total+=current 

    return total

print(roman_to_integer("XL"))







