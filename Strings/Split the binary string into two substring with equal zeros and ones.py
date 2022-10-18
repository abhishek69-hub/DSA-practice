a="0100110101"
count0=0
count1=0
countmax=0
for i in range(len(a)):
    if a[i] == "0":
        count0 = count0 + 1
        if count0 == count1 and count0>0:
            countmax = countmax + 1
            count0 = 0
            count1 = 0
        elif count0 != count1:
            continue

    elif a[i] == "1":
        count1 += 1
        if count0 == count1 and count1>0:
            countmax = countmax + 1
            count0 = 0
            count1 = 0
        elif count1 != count0:
            continue

print(countmax)
# print(count0)
# print(count1)
# print(a[i])
