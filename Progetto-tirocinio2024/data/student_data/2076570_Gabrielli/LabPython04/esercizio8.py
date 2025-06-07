s1=input('inserisci una stringa: ')
s2=input('inserisci una stringa: ')
while True:
    if s1[len(s1)-1]==s2[0]:
        break
    s1=s2
    s2=input('inserisci una stringa: ')
print(s1+', '+s2)
