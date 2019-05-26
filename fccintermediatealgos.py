def destroyer(arr, clear):
    length = len(arr)
    for item in range(length):
        if item in clear:
            arr.remove(item)
    print(arr)

destroyer([1,2,3,4,5],[3,2,4])