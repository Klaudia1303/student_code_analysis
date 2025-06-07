s=input('inserire una stringa:')
finale= s[-1]
finito= False
while not finito:
    s1=s
    s=input('inserire una stringa:')
    iniziale= s[0]
    if finale==iniziale:
        finito=True
        s2=s
    else:
        finale=s[-1]
print(s1,s2)
