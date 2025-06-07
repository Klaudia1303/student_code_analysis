s=input('inserisci un anno:')
s=int(s)
if((s%4==0) and(s%100!=0)):
    print('anno bisestile')
else:
    print('anno non bisestile')
