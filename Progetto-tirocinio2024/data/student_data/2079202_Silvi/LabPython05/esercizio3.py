s1=input("inserire la prima stringa: ")
s2=input("inserire la seconda stringa: ")

for i in range(0,len(s1)):
    if s2.find(s1[i])==-1:
        print(s1[i],end="")
