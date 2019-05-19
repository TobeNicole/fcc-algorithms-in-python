# FREE CODE CAMP BASIC ALGORITHM SCRIPTING PYTHON SOLUTIONS

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


def largest_num(num):
    answer = 0
    for i in range(len(num)):
        if (num[i]>= answer):
            answer = num[i]
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
    for i in range(len(mystr_arr)):
       final_arr.append(mystr_arr[i].capitalize()) 

    print(' '.join(final_arr))

# title_case('hello DARKNESS mY oLD friend')

def franken_splice(arr1, arr2, n):
    index = n
    for i in range(len(arr2)):
        arr1.insert(index,arr2[i])
        index+=1
    print(arr1)
    

# franken_splice([1,2,3], [4,5], 1)

def get_index_to_insert(arr, n):
    new_arr = arr[:] #copy the list by slicing, apparently assigning a list to a new var doesn't actually copy it. They reference same thing in mem
    item = 0 
    for i in range(len(new_arr)):
        if( new_arr[i] < n  ):
            item = new_arr[i]
    for i in range(-1,- len(arr), -1): #start from last index 
        if(arr[i] == item):
            print( (len(arr) - abs(i) ) + 1 )
            break

get_index_to_insert([1,3,5, 4,6,], 8)

