s1=str(input('Inserisci una stringa:'))
s2=str(input('Inserisci una stringa:'))

c=''
if len(s1)==len(s2):
    for i in range(len(s1)):
        c=(s1[i]+s2[i])
        print(c,end="")
