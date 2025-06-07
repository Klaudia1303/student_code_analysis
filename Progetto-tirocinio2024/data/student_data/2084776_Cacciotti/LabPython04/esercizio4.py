false=0
i=1
contn=0
while i>0:
    s=int(input('inserisci un numero'))
    if s!=0:

        if s%3==0:
            contn+=s
    else:
        i=-1

print(contn)
