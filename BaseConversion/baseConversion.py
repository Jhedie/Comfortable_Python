#not an exhaustive solution
def toHex(number, base):
    
    if base != 10:
        result = int(number[0])
        for i in range(1, len(number)):
            result = result * base + int(number[i])
    else:
        result = int(number)

    remainders = []
    while result > 0:
        remainder = result % 16
        remainders.append(remainder)
        result = result // 16
    
    HexLetters = {10:'a', 11:'b',12:'c',13:'d', 14:'e', 15:'f'}
    hexValue = ""
    for i in range(len(remainders)-1, -1, -1):
        if remainders[i] <= 9:
            hexValue += str(remainders[i])
        
        else:
            hexValue += HexLetters[remainders[i]]
    print(hexValue)            


#method 2
def toHex1(number, base):
    #convert into base 10
    # int(number, base)
    number = int(number, 5)
    print(number)
    #convert into hex, gives format '0x'...
    #slice leading '0x'
    print(hex(number)[2:])
    




test1 = "1302"
test2 = "5815"
toHex1(test1, 5)

