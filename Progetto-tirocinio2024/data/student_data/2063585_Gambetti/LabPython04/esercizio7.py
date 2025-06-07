s=input('inserisci una stringa: ')
i=0
finito=False
momento=0
while i<len(s):
    n=s.count(s[i])
    if n>=momento:
        momento=n
        l=s[i]
    i+=1
print(l)
        
   
