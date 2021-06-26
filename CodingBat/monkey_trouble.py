#https://codingbat.com/prob/p120546

#My method
def monkey_trouble(a_smile, b_smile):
    if (a_smile == True and b_smile) or (a_smile == False and b_smile == False):
        return True
    return False

#Method 2:
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not(a_smile) and not(b_smile):
        return True
    return False

#Method 3:
def monkey_trouble(a_smile, b_smile):
    return ((a_smile and b_smile) or (not a_smile and not b_smile))

#Method 4 (Most efficient):
def monkey_trouble(a_smile, b_smile):
    return(a_smile == b_smile)


