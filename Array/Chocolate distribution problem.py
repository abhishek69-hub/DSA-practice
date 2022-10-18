def chocolate(arr,m):
    n=len(arr)
    arr.sort()
    md=arr[n-1]-arr[0]
    for i in range(0,n-m+1):
        md=min(md,arr[i+m-1]-arr[i])
    return md



print(chocolate([7, 3, 2, 4, 9, 12, 56],m=4))