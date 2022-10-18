arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]
n=len(arr1)
m=len(arr2)

while arr1[n-1] > arr2[0]:
    temp=arr1[n-1]
    arr1[n-1]=arr2[0]
    arr2[0]=temp
    arr1.sort()
    arr2.sort()
print(arr2)
print(arr1)