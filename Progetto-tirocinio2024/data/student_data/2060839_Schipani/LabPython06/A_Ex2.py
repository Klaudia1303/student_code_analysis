s=input('inserisci una stringa ')
i=0
f=len(s)-1
liv=0
while i<=int(len(s)+1)/2:
    if s[i]==s[f]:
        liv+=1
        f-=1
        i+=1
    else:
        break
if i>=(f/2):
    liv=len(s)
print('livello di palindromicità ',liv)
