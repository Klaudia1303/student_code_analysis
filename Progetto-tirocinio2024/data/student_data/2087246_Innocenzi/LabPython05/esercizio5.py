s=input("Inserisci una stringa con almeno due caratteri: ")
n=int(input("Inserisci un numero intero: "))
k=0
for i in range(len(s)): 
        if(n+i<len(s)):
                if((s[i])==(s[i+n])):
                        k=1

if(k==1):
        print("True")
else:
        print("False")
                
