n=int(input('Inserire la base di un triangolo isoscele("intero dispari >= a 3"):'))
for i in range (n+1):
    if i%2!=0:
        print(((n-i)//2)*' ','*'*i)
