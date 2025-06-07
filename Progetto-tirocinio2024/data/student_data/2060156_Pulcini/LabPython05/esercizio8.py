base=int(input('inserire la base del triangolo isoscele:'))
j=(base//2)-1
if base%2!=0 and base>=3:
    for i in range(1,base,2):
        print(' '*(j),'*'*(i))
        j-=1
    print('*'*base)
        
