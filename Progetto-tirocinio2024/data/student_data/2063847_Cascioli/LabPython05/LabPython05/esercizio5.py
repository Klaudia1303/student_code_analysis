s=''
while(len(s)<2):
    s=input("Inserire una stringa con almeno due caratteri:")
n=int(input("Inserire un numero intero:"))
for i in  range (len(s)-n):
       if (s[i]==s[i+n]):
            cond=True
       else:
            cond=False
print(cond)

    
