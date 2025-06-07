s = str(input("Inserire una stringa con almeno due caratteri:"))
n = int(input("Inserire un numero intero positivo:"))
r = False

for i in  range(len(s)-n):
   if s[i] == s[i+n]:
       r = True
print(r)
    
    
    
