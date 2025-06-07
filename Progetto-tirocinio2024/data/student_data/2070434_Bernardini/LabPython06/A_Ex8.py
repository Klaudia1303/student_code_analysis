s1=input('inserire stringa: ')
s2=input('inserire stringa: ')
n=int(input('inserire numero: '))
somma=' '
for i in range(len(s1)):
    a=int(i-n)
    b=int(i+n)
    if s1[i] in s2[a:b]:
        somma +=s1[i]
print(somma)
