'''
String manipulation exercises
Vincent Stevenson
https://medium.com/javarevisited/top-21-string-programming-interview-questions-for-beginners-and-experienced-developers-56037048de45
'''

def reverse_string(s):
    '''
    Sample usage:
    s = 'vincent'
    rev_s = reverse_string(s)
    print('String: {}, reversed string: {}'.format(s, rev_s))
    '''
    # reverse a given str
    i = len(s) - 1
    rev_s_chars = []  # init empty str
    while i >= 0:
        rev_s_chars.append(s[i])
        i -= 1
    rev_s = ''.join(rev_s_chars)
    return rev_s

def print_dup_str_chars(s):
    '''
    'aaa' should print a
    'abbc' should print b
    'aabcc' should print a, c

    s = 'abcdd'
    print_dup_str_chars(s)
    '''
    # init a dict to persist char and char count of str
    # key = char, value = char_count in str
    print('Original string: {}'.format(s))
    char_dict_counter = {}
    for char in s:
        # if the char is already in the dict, increment the count
        if '{}'.format(char) in char_dict_counter:
            char_dict_counter['{}'.format(char)] += 1
        # else init it to 1
        else:
            char_dict_counter['{}'.format(char)] = 1
    for k, v in char_dict_counter.items():
        if v > 1:
            print('Char {} shows up {} times'.format(k,v))

def check_if_anagram(a,b):
    # persist the chars for the two strings in dicts
    # dicts will allow for hash lookups
    # return true if two strings are anagrams
    # char count must be identical between two strings
    '''
    a = 'secure'
    b = 'rescue'
    check_if_anagram(a,b)
    '''
    a_dict = create_char_dict(a)
    b_dict = create_char_dict(b)
    # note that the sequence of keys doesn't matter, as long as the keys exist and the values are the same for both dicts, you can use the == operator
    if a_dict == b_dict:
        print('{} and {} are anagrams'.format(a,b))
        return True
    else:
        return False

def create_char_dict(s):
    # persist the char and char_count of a string in a dict as key-value pairs
    char_dict = {}
    for char in s:
        if '{}'.format(char) in char_dict:
            char_dict['{}'.format(char)] += 1
        else:
            char_dict['{}'.format(char)] = 1
    return char_dict

def is_palindrome(s):
    # return true if the word reads same backwards as forwards
    '''
    s = 'nurses run'
    is_palindrome(s)
    '''
    rev_char_list = []
    s_len = len(s) - 1
    i = s_len
    while i >= 0:
        if s[i].isalpha():
            rev_char_list.append(s[i])
        i -= 1
    char_list = []
    for j in s:
        if j.isalpha():
            char_list.append(j)

    if char_list == rev_char_list:
        print('{} is a palindrome.'.format(s))
        return True
    else:
        return False


s = 'abc'
result = []
def permute(arr, i, length):
    # base case
    if i == length:
        # join method puts all items in an iterable into one string
        result.append(''.join(arr))
    else: # recursive case
        for j in range(i, length):
            # swap the elem positions within the array
            arr[i], arr[j] = arr[j], arr[i]
            permute(arr, i+1, length)

# prints out a list of all permutations of a string:
permute(list(s), 0, len(s))
print(result)