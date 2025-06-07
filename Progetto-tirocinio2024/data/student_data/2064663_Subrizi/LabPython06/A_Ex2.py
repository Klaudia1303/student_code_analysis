s=input('Inserisci una stringa: ')
grado=0

for i in range(len(s)//2+1):
    if s[i]!=s[-(i+1)]:
        break
if i==len(s)//2 and len(s)%2!=0:
    i+=1
if i==0:
    print(' La stringa non è palindroma')
elif i>0:
    print('La stringa è palindroma di grado', str(i))
elif s==s[::-1]:
    print('La stringa è palindroma')
    
