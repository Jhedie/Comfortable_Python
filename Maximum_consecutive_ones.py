'''Given a binary array, find the index of the 0
to be replaced with 1 to get the maximum length
sequence of continuous ones.
https://www.techiedelight.com/find-index-0-replaced-get-maximum-length-sequence-of-continuous-ones/
'''

#Use sliding window approach
#Helpful Notes
'''
1. Think more about the indexes of the list rather than the actual values
2. Read description carefully
3. Try very slow dry running.

'''
def countMaxConsecutive_1s(an_array):
    max_ones = 0 #which stores the maximum number of ones
    max_index = 0 # index of maximum number of ones
    
    counter = 0  # counts the number of 1s
    prev_zero_index = 0 # assumes this is changed to a 1

    current_index = 0
    #traverse through the array
    while current_index < len(an_array):
    #if we see a 1 we add one to count until we see and zero.
        if an_array[current_index] == 1:
            counter += 1 # store the count if its the maximum seen so far
        else:
            
            #if we see a zero,
             #we set the counter to the space count between the current index
              #and the previous index 
            counter = current_index - prev_zero_index

            #we then update the index of the previous zero to the current zero we have found 
            prev_zero_index = current_index
        if counter > max_ones:
            max_ones = counter
            # change the index to where the zero was flipped which is the first zero we saw in every case 
            max_index = prev_zero_index
            
        current_index += 1
    return max_index

    
array = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1 ]
print(countMaxConsecutive_1s(array))
