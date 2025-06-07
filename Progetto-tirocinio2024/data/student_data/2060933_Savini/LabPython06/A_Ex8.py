s1=input('inserisci la stringa: ')
s2=input('inserisci la stringa: ')
n=int(input('inserisci intero: '))
l=''
for i in range (len(s1)) :
    for k in range(len(s2)):
        if s1[i]==s2[k] and abs(i-k)<=2:
            l=l+s1[i]
print(l)
