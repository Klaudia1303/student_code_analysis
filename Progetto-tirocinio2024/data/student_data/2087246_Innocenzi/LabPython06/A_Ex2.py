s=input("Inserisci una stringa: ")
k=0
s1=s[::-1]
if(s==s1):
    print(len(s))
else:
    for i in range(len(s)//2):
        if(s[i]==s[-1-i]):
            k+=1
    print(k)