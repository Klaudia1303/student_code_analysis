s=input("Inserisci una stringa contenente almeno due caratteri: ")
n=int(input("Inserisci un intero positivo: "))
temp=0
for i in range(len(s)-n):
    if s.count(s[i])==2:
        if s[i+n]==s[i]:
            print("True")
            break
        else:
            temp+=1
    else:
        temp+=1
if temp==len(s)-n:
    print("False")
        
