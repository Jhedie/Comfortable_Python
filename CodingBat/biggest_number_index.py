# program to print the index of the biggest number in an array


#main function
def get_biggest(array):
    position = 0
    return biggest_number(array, position)



#recursive function for comparisons
def biggest_number(List, position1):
    if position1 == len(List)-1:
        return position1
    else:
        #position2 which we would compare with position 1
        position2 = biggest_number(List, position1 + 1)
        #if position2 is bigger we maintain position2
        if List[position2] > List[position1]:
            return position2
        #otherwise position1 is maintained
        else:
            return position1
list1 = [9, -20, 6, 1, 80, 9, 2]

print(get_biggest(list))


