str1=input()
str2=input()
str3=input()
str4=str1+str2
str5="".join(sorted(str4))
str6="".join(sorted(str3))
print(str6)
print(str5)
if str5 == str6:
    print("Valid shuffle")
else:
    print("INvalid shuffle")