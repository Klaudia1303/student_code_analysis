s1=input("Inserire la prima stringa: ")
s2=input("Inserie la seconda stringa: ")
stot=''
for i in range(len(s1)):
    v=s1[i]
    if s2.find(v)==-1:
            stot=stot+s1[i]
print(stot)
