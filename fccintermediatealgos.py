def destroyer(arr, clear):
    length = len(arr)
    for item in range(length):
        if item in clear:
            arr.remove(item)
    print(arr)

# destroyer([1,2,3,4,5],[3,2,4])

def what_is_in_a_name(collection, source):
        keys = source.keys()
        arr = []
        match_count = 0
        for item in collection:
                for key in keys:
                        if item[key] == source[key]:
                                match_count += 1
                if match_count == len(keys):
                        arr.append(item)
        print(arr) 

# what_is_in_a_name([{ 'first': "Romeo", 'last': "Montague" }, { 'first': "Mercutio", 'last': 'null' }, { 'first': "Tybalt", 'last': "Capulet" }], { 'last': "Capulet" })

def is_prime(num):
  for i in range(2,num, 1):
    if (num % i == 0):
      print(False) 
      return
  print(True)
  return
# is_prime(20)


def pig_latin(str):
        vowels = ['a','e','i','o','u']
        consonant = True if str[0] not in vowels else False
        suffix = 'ay' if consonant else 'way'
        for s in str:
                if s in vowels:
                        insert = str[:str.index(s)]
                        return str[str.index(s):] + insert + suffix

# print( pig_latin('glove'))


def sum_primes(num):
        total = 0
        i = 2
        prime = False
        while i <= num:
                for divisor in range(2, (i+1), 1): 
                        if i % divisor == 0 and i != divisor:
                                i+=1
                                break
                        elif i == divisor:
                                prime = True
                                break     
                if prime:
                        total += i
                        i+=1
                        prime = False
        return total


print(sum_primes(10))
