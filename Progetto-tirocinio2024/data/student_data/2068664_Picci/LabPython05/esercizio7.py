s=input('inserisci una stringa:')
c=True
for i in s:
    if s.count(i)>1 and c:
        print('True')
        c=False
if c==True:
    print('False')



        
