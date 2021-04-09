'''
Write a Python program to remove and
print every third number from a list
of numbers until the list becomes empty
'''

def remove_Third(sequence):
    next_interval = 2#index of third number
    index = 0
    list_length = len(sequence)
    
    while list_length > 0:
        print(sequence)
        # find the next 3rd position by adding the interval and bound it with the length of the list
        # bounding is done using modulos of the list
        index = (next_interval + index) % list_length
        
        print("next index: "  + str(index) + " list size:  " + str(list_length))
        print()
        print("Remove: " + str(sequence.pop(index)))
        list_length -= 1
        
        
test_sequence = [10, 20, 30, 40, 50, 60, 70, 80, 90]

remove_Third(test_sequence)
