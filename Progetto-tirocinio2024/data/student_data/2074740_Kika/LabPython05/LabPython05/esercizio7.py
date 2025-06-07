s=input('inserisci stringa: ')
c=1
i=0
while c==1 and i<len(s):
        c=s.count(s[i])
        if c>1:
            print('true')
        else:
            i=i+1
if c==1:
    print('false')
