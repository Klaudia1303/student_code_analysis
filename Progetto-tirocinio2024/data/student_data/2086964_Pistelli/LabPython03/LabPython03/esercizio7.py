a=input('inserire un carettere ')
c=True
while c:
    b=str(input('inserire una stringa '))
    if b.count(a)>=2:
        print(b.count(a))
        c=False
    
