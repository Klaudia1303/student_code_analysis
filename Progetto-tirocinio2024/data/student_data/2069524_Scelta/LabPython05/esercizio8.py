bti=int(input('Inserisci la base di un triangolo isoscele come n dispari>=3:'))
for i in range(bti+1):
    if i%2!=0:
        print(((bti-i)//2)*' '+'*'*i)
        
