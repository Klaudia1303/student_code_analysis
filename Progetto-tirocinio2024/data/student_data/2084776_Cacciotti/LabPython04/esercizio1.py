true=True
i=0
a=0
while true:
    s=input('inserisci una stringa')
    if s.find('a')!=-1 and s.find('c')!=-1:
        a=a+1
        true=False
    else:
        a+=1
print(a)
