'''
Write a Python program to find unique triplets whose three elements
gives the sum of zero from an array of n integers.
'''
#time complexity is O(n ^3) : not very efficient 
def unique_triplets(alist):
    
    for i in range(len(alist)-2):
        for j in range(i+1, len(alist)-1):
            for k in range(j+1, len(alist)):
                if alist[i] + alist[j] + alist[k] == 0:
                    print(alist[i],alist[j],alist[k])


#Efficient solution, solved in O(n)


def unique_triplets2(alist):
    triplets = []
    
    alist = list#sort the given array
    print(alist)
    found = False 
    #traverse the array
    for a in range(len(alist)-2):
        
    #set a left and right variable
        l = a + 1
        r = len(alist) - 1
        
        while (l < r):
            #for every current element during traversal, a solution is found if the sum of the left, right = the current element
                if (alist[a] + alist[l] + alist[r] == 0):
                    triplets.append((alist[a], alist[l], alist[r]))
                    l += 1
                    r -= 1
                    found = True
            #since sorted we can determine the direction to move into,
            #if the pair sum is greater than the sum(0) we can shift the right one step back to draw closer to the intended number
                elif (alist[a] + alist[l] + alist[r] > 0):
                    r -= 1
            #the same happens for left side untill the left > right.
                else:
                    l += 1
    if len(triplets) == 0:
        return "No triplet Found"
    else:
        return triplets
test1 = [1,-6, 4, 2, -1, 2, 0, -2, 0]
test2 = [0, -1, 2, -3, 1]
print(unique_triplets2(test2))
