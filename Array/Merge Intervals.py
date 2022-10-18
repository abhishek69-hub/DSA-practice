arr1=[[6, 8], [1, 9], [2, 4], [4, 7]]
i=1
arr1.sort()
print(arr1)
while i <= len(arr1)-1:
    if arr1[i - 1][1] > arr1[i][0]:
        if arr1[i - 1][0] < arr1[i][0]:
            arr1[i][0] = arr1[i - 1][0]

        if arr1[i - 1][1] > arr1[i][1]:
            arr1[i][1] = arr1[i][1]
        else:
            arr1[i][1] = arr1[i][1]
        arr1.remove(arr1[i - 1])
        i = i
    else:
        i = i + 1
print(arr1)