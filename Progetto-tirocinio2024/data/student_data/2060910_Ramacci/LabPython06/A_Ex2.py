s=input("inserire una stringa: ")
r=0
p=-1
if str(s)==str(s)[::-1]:
    print(len(s))
else:
    for i in range(len(s)):
        while s[r]==s[p]:
            r+=1
            p-=1
        print("il livello di periodicità è",r)
        break
