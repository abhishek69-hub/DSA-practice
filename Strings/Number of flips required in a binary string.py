s="000001100"
count0=0
count1=0
count=0
for i in range(len(s)):
    if i%2 == 0 and s[i]=="0":
        count0 += 1
    if i%2 == 1 and s[i]=="1":
        count0 += 1

for i in range(len(s)):
    if i%2 == 0 and s[i]=="1":
        count1 += 1
    if i%2 == 1 and s[i]=="0":
        count1 += 1

if count0 > count1:
    for i in range(len(s)):
        if i % 2 == 0 and s[i] == "1":
            count += 1
        if i % 2 == 1 and s[i] == "0":
            count += 1

elif count0 < count1:
    for i in range(len(s)):
        if i % 2 == 1 and s[i] == "1":
            count += 1
        if i % 2 == 0 and s[i] == "0":
            count += 1


print(count)
print(count1)
print(count0)