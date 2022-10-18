str="abey saale abey"
arr1=str.split()
print(arr1)
for i in arr1:
    if arr1.count(i) > 1:
        arr1.remove(i)
        print(i)
        break