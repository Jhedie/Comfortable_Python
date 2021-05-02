

'''Find the smallest missing positive number from an unsorted array'''
#METHOD 1. 
def  min_missing_positive(an_array):

    
    missing_numbers = {*an_array}

    print(missing_numbers)
    index = 1
    while True:
        if index not in missing_numbers:
            return index
        index += 1

    return index




#METHOD TWO

'''
Helpful tips
1. Try to dry run code
2. Steps:
        first segregate
        pick out positives
        find missing positives
3. Considering index within array really helps.
'''
#Segregate(separate positives from negatives)
def segregate(arr):

    positive_index = 0
    
    for curr_index in range(len(arr)):
        #if the current number is 0 or negative, we swap it with the current positive number
        if arr[curr_index] <= 0:
            arr[curr_index], arr[positive_index] = arr[positive_index], arr[curr_index]
            # after swapping the value of positive index will be negative therefore +1
            positive_index += 1 
    
    return positive_index



#Find Minimum smallest
def min_missing_positive1(arr):

    #index of starting positive number in list
    pos_index_start = segregate(arr)
    #list of all positives
    seg_list = arr[pos_index_start:]
    print(seg_list)


    for number in range(len(seg_list)):
        
        curr_value = abs(seg_list[number])
        #first case checks whether current element is in the list range
        #second case checks if value at position curr_value has not been negated yet
        if curr_value - 1 < len(seg_list) and seg_list[curr_value - 1] > 0:
            seg_list[curr_value-1] = -seg_list[curr_value-1]
            print(seg_list)

    for i in range(len(seg_list)):
        if seg_list[i] > 0:
            return i + 1
    #no missing elements within which means the smallest positive number to be added must be the next number in sequence
        #which is not included in the list.
    return len(seg_list)+1
    




test1 = [-1, 4, 2, -2, 6, 5]

test2 = [-1,-2,-3,-4]
print(min_missing_positive1(test1))
