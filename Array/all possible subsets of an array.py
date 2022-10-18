arr=[1,2,3,4]

def subset(arr,subset,ans,x):
    if x==len(arr):
        ans.append(subset)
        return[[]]


    partialanswer=subset(arr,subset,ans,x+1)
    ans = map(append, )
    ans = map(lambda x, y: x.append(y), partialanswer, arr[x])



