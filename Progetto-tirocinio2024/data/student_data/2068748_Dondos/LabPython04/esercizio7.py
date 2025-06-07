s=input('Inserisci una stringa: ')
c_max=0
i=0

while i<len(s):
    if s.count(s[i])>=c_max:
        c_max=s.count(s[i])
        find=i
    i+=1
print(s[find])
