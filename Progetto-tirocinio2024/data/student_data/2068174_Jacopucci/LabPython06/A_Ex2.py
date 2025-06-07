s=input('inseire una stringa palindroma: ')
c=1
i=0
n=0
while i!=len(s):
    if s[i]==s[-(i+1)]:
        n+=1
        i+=1
    else:
        i+=1
print('il livello di palindormicità è: '+ str(n))
