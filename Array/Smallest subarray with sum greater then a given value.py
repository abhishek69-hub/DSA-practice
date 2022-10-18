def smallest(arr,m):
    n=len(arr)
    arr2=[]
    sum=0
    for i in range(0,n):
        if arr[i]>m:
            return arr[i]
        else:
            arr2.append(arr[i])


