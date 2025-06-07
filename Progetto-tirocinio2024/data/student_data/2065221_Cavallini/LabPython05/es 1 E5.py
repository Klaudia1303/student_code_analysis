s1 = input('inserisci una stringa: ')
s2 = input('inserisci una stringa della stessa lunghezza: ')
sf=''
for i in range (len(s1)):
    sf+=(s1[i]+s2[i])
print(sf)
