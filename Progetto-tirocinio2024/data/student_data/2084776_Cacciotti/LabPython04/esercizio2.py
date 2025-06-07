false='*'
i=0
contn=0
while i>=0:
    s=input('inserisci un numero')
    if s!='*':
        n=int(s)
        if n>=0:
            contn=contn+1
    else:
        i=-1
print(contn)
