base=int(input('Inserire una base dispari di un triangolo isoscele: '))
c=base//2
for i in range(1,base+1,2):
    print(c*' '+i*'*')
    c-=1
