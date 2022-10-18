arr1=[7, 1,20, 5, 3, 6, 4,19]
buy=arr1[0]
max_profit=0
for i in range(1,len(arr1)):
    if buy>arr1[i]:
        buy = arr1[i]
    elif (arr1[i] - buy) > max_profit:
        max_profit = arr1[i] - buy

print(max_profit)
