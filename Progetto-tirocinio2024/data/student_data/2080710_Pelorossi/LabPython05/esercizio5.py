s=input('inserisci una stringa:')
n=int(input('inserisci un intero positivo:'))
tot=0
for i in range(len(s)-n):
    if s[i]==s[i+n]:
        tot+=1
if tot>=1:
    print(True)
else:
    print(False)
