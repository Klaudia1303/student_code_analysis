s1=input('Inserisci una stringa: ')
s2=input('Inserisci una stringa: ')
s=''
for i in range(len(s1)):
    for j in range(i,len(s1)):
        if s1[i:j+1] in s2:
            if len(s1[i:j+1])>=len(s):
                   s=s1[i:j+1]
            else:
                break
print(s)
