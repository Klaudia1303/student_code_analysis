s1=input("immetti prima stringa: ")
s2=input("immetti seconda stringa: ")
for i in s1:
    if s2.find(i)==-1:
        print(i,end="")
