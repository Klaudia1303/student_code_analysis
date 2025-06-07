finish=False
while finish==False:
    n=int(input('inserisci lato quadrato'))
    for i in range(1,n+1):
        if i==1 or i==n:
            print('*'*n)
        else:
            print('*',(n-4)*' ','*')
m=input('finish?(Yes/No)')
if m.lower()=='yes':
    finish=True
