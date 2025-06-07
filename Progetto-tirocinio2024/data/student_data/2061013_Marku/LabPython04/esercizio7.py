s=input('inserire stringa: ')
i=0
n=0

while len(s)>i:
    carattere=s.count(s[i])
    if carattere>=n:
        n=carattere
        c=s[i]
    i+=1
print(c)
   
