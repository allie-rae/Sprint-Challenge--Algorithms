'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # length of input
    len_word = len(word)
    # substring of interest
    substring = "th"
    # length of substring
    len_substring = len(substring)
    # if there's no more input left, return
    if len_word == 0:
        return 0; # base case    
    # if the first 2 letters are "th", 
    # add 1 to the "th" count
    # then rescursively move on by
    # removing the first letter from the input and
    # calling the function on that new "word"
    if(word[0:len_substring] == substring):
        return count_th(word[1:]) + 1
    # if they are not "th", do the same
    # thing as above but do not add to the count
    return count_th(word[1:])
