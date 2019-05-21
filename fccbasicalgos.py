# FREE CODE CAMP BASIC ALGORITHM SCRIPTING PYTHON SOLUTIONS

import math


def reverse_string(mystr):
    newStr = ''
    for i in range((len(mystr) -1),-1,-1):
        newStr += mystr[i]
    print(newStr) 

# reverse_string('rachel')

def factorialize(num):
    product = 1
    for i in range(1,num+1):
        product *= i
    print(product)

# factorialize(5)

def longest_word(word):
    str_arr = word.split(' ')
    # print( len(  str_arr))
    answer = ''
    for i in range(len(str_arr)):
        if (len(str_arr[i]) > len(answer)):
            answer = str_arr[i]
    print(answer)

# longest_word('The trees in spain grow primarily in the rain')


def largest_num(nums):
    answer = 0
    for num in nums:
        if (num >= answer):
            answer = num
    print(answer)

# largest_num([1,500,6,-1,300])

def ends_with(mystr, target):
    target_length = len(target) 
    # str_compare = str[-1: -target_length]
    str_compare = mystr[-target_length:]
    print(str_compare)
    if(str_compare == target):
        print('true')
    else:
        print('false')
    
# ends_with('hey here', 'here')

def repeat_string(mystr, num):
    print(mystr * num)

# repeat_string('hello', 3)

def truncate(mystr, length):
    str_slice = mystr[:length]
    print(str_slice +  '...')

# truncate('hello', 2)

def find_function(arr, test_function):
    for i in range(len(arr)):
        if (test_function(arr[i])):
            print(arr[i])
            break
    # return 'undefined'

def into_six(a): #Test function
    print('into_six string')
    if(6 % a ==0):
        return True

# find_function([4,5,2,6], into_six)

def is_bool(boo):
    if(boo == True or boo == False):
        print('True')
    else:
        print('False')

# is_bool('not')

def title_case(mystr):
    normalized_str = mystr.lower()
    mystr_arr = normalized_str.split(' ')
    final_arr = []
    for string in mystr_arr:
       final_arr.append(string.capitalize()) 

    print(' '.join(final_arr))

# title_case('hello DARKNESS mY oLD friend')

def franken_splice(arr1, arr2, n):
    for i in arr2:
        arr1.insert(n,i)
        n+=1
    print(arr1)
    

# franken_splice([1,2,3], [4,5], 1)

def get_index_to_insert(arr, n):
    new_arr = arr[:] #assigning a list to a new var doesn't actually copy it. new_arr & arr reference same list in mememory
    item = 0 
    for i in range(len(new_arr)):
        if( new_arr[i] < n  ):
            item = new_arr[i]
    for i in range(-1,- len(arr), -1): #start from last index 
        if(arr[i] == item):
            print( (len(arr) - abs(i) ) + 1 )
            break

# get_index_to_insert([1,3,5, 4,6,], 8)

def mutations(arr):
    str1 = arr[0]
    str2 = arr[1]
    count = 0
    for i in range(len(str2)):
        for index in range(len(str1)):
            if(str1[index] == str2[i]):
                count += 1
                break
    if(count == len(str2)):
        print('True')
    else:
        print('False')
# mutations(['hello', 'nell'])


def chunky_monkey(arr, num):
    start = 0 #update the slice position through start and end variables
    end = num  
    chunked_arr = [] #we'll place chuncked arrays here
    floated = (len(arr)/num) +1  
    count = floated if len(arr) % num  != 0 else floated -1 #this gives how many times we need to loop through to chunk array completely
    for _ in range(count): 
        if(end < (len(arr))): 
            chunked_arr.append(arr[start:end])
            start += num
            end += start
        else:
            chunked_arr.append(arr[start:])
    print(chunked_arr)

# chunky_monkey([2,3,4,5,6], 4)



