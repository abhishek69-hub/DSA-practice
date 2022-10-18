a="forgeeksskeegfor"
real=[]
palin=[]
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        real.append(a[i:j])

def ispalindrome(str):
    stack = []
    str1=""
    for i in range(len(str)):
        stack.append(str[i])
    for j in range(len(str)):
        str1 += stack.pop()
    if str == str1:
        return True
    else:
        return False

for i in real:
    if ispalindrome(i) == True:
        palin.append(i)

# print(len(palin))
maxlen=0
ans=[1]
for i in range(len(palin)):
    if len(palin[i]) > maxlen:

        maxlen=len(palin[i])
        ans[0] = palin[i]

print(ans[0])





