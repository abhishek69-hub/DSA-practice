a = input()
leng = len(a)
s = set()
for i in range(leng):
    if a[i] in s:
        print(a[i]+" " +"is a duplicate")
    else:
        s.add(a[i])
        continue
