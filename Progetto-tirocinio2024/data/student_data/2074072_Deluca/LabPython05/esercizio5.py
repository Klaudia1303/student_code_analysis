s=input("inserisci stringa: ")
n=int(input("inserisci numero: "))
corretto=False
for i in range(0,len(s)-n):
    if s[i]==s[i+n]:
            print("True")
            corretto=True
if corretto==False:
     print("False")
                
        
