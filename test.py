def first_recurring(arr1):
    seen = set()
    for num in arr1:
        if num in seen:
            return num
        seen.add(num)   
    return -1

arr1 = [0, 3, 4, 2, 3]
arr2 = [1, 5, 7]
print(first_recurring(arr1))