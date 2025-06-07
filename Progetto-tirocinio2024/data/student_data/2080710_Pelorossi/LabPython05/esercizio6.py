s=input('inserisci una stringa:')
n=0
for i in range(len(s)):
    x=int(s.rfind(s[i]))- int(s.find(s[i]))
    if x>n:
        n=x
print(n)
        
