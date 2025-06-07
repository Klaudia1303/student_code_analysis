n=int(input('inserire la base di un triangolo isoscele>=3: '))
if n>=3 and n%2!=0:
    for i in range(n+1):
        if i%2!=0:
            print(((n-i)//2)*' ','*'*i)

    

