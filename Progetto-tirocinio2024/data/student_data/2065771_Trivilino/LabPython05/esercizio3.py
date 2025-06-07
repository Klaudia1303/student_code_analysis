s1=input('Inserire una stringa: ')
s2=input('Inserire una seconda stringa: ')
f=''
for i in s1:
    if s2.count(i)==0:
        f+=i
print(f)
