x=str(input('inserisci stringa: '))
for i in range(0,len(x)):
    if x[i]!=x[len(x)-1-i]:
        break
if i==0: print('parola non palindroma livello 0')
elif x==x[::-1]: print('parola palindroma livello',len(x))
else: print('parola palindroma livello',i)
    
  
