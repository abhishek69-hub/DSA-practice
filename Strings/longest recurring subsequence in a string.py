digit=534976
a=[5,3,4,9,7,6]
n=6
for i in range(n-1,0,-1):
    if a[i-1]<a[i]:
        var1=a[i-1]
        break

for j in range(n-1,i,-1):
    if a[j]>a[i-1]:
        a[i-1]=a[j]
        a[j]=var1
        break
x=0
for k in range(i):
         x = x * 10 + a[k]
a = sorted(a[i:])
for j in range(n-i):
         x = x * 10 + a[j]

print(a)
print(x)
    