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

what_is_in_a_name([{ 'first': "Romeo", 'last': "Montague" }, { 'first': "Mercutio", 'last': 'null' }, { 'first': "Tybalt", 'last': "Capulet" }], { 'last': "Capulet" })