s1=input('inserisci una stringa: ')
s2=input('inserisci una stringa: ')
br=False
for i in range(len(s1)-1,1,-1):
    for j in range(len(s1)-i+1):
        if s1[j:i+j] in s2:
            print(s1[j:i+j])
            br=True
            break
    if br:
        break




