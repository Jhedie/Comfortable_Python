'''
Write a Python program to create all permutations strings by using #
'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
'''
#using itertools
def swap(alist, curr, choice):
    alist[curr], alist[choice] = alist[choice], alist[curr]



def permutation(alist, current_index= 0):
    #once the current_index is equal to the last index which is the length(alist)
    #print the string.
    if current_index == len(alist)-1:
        print(''.join(alist))
    #from the current_index to the last element index
    for choice_index in range(current_index, len(alist)):
        
        swap(alist, current_index, choice_index)

        #recurse with the list and the next element from the current index
        permutation(alist, current_index + 1 )


        #choices are exhausted now backtrack/swap back
        swap(alist, current_index, choice_index)

permutation(["A","B","C"])
    
