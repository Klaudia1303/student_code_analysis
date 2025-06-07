s1= input('inserisci una stringa')
s2= input('inserisci una stringa')
i=0

snuova=' '
if len(s1)==len(s2):
    for i in range(0,len(s1)):
        snuova=snuova+s1[i]+s2[i]
    print(snuova)
