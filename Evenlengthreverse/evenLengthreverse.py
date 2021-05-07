def evenLengthReverse(string):
    result_string = ""
    string = string.split()
    for i in string:
        string_length = len(i)
        if string_length  % 2 ==0:
            result_string += i[::-1]
        else:
            result_string += i
        result_string += " "
    print(result_string)
            


    
test1 = "The quick brown fox jumps over the lazy dog"
test2 = "Python Exercises"

evenLengthReverse(test1)
evenLengthReverse(test2)
