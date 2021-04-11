'''
Write a Python function that takes a sequence of numbers
and determines whether all the numbers are different from each other.
'''
def is_All_different(alist):
    buffer = []
    for i in alist:
        if i in buffer:
            return False
        else:
            buffer.append(i)
    return True

#alternative method
def is_All_different2(alist):
    '''
    set function removes all repetitions
    if there are no repetitions, set(alist) must have the same length
    as original list
    '''
    if len(alist) == len(set(alist)):
        return True
    else:
        return False
    
numbers = [1,2,4,5]
print(is_All_different2(numbers))
