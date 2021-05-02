#reverse in parenthesis
#Codefights Arcade problem
'''
Write a function
that reverses characters in (possibly nested)
parentheses in the input string.
'''

#first method
#This can be done using a stack



def reverseParenthesis(string):
    stack = [""]


    # run through every character in the array.

    for char in string:
        if char == "(":
            #put an empty string onto the stack
            stack.append("")
        elif char == ")":
            #a set has been obtained therefore pop it in reverse order and then add to the first empty element
            current_string = stack.pop()[::-1]
            #push current_string unto the stack
            stack[-1] += current_string
            
        else:
            #add the character the stack
            stack[-1] += char
    return stack.pop()

def reverseParenthesis2(string):
    for char in range(len(string)):
        #on encountering a '(' #save its index
        if string[char] == "(":
            start = char
        #once we see ')' we save its index
        if string[char] == ")":
            end = char
            #reverse the string between the first and last
            #pass the new string into the function reverseParenthesis

            # string format : all characters from beginning of string till the first '('
            #                   the reversed string between the start and end
            #                       the remaining part of the string from the ')' to the remaining part of the main string
            return reverseParenthesis2(string[:start] + string[start+1:end][::-1] + string[end+1:])
    return string

        

test1 = '(foobar)baz(blim)'
test2 = '(rab)'
test3 = 'i(evol)you'
print(reverseParenthesis2(test3))
    
#second Method

#Use recursion


