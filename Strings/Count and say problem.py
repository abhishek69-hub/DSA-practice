
def countandsay(n):
    if (n==1):
        return 1
    if(n==2):
        return 11
    str1="11"

    for i in range(3,n+1):
        str2 = " "
        str1=str1+"$"
        counter=1
        for j in range(1,len(str1)):
            if(str1[j] != str1[j-1]):
                str2 += str(counter)
                str2 += str1[j-1]
                counter = 1
            else:
                counter += 1
        str1=str2
    return str1

print(countandsay(5))

