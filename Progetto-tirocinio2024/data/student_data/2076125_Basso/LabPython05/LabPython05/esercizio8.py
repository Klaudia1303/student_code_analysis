

b=int(input("Inserire base triangolo isoscele:\t"))
c=b//2

for i in range(1,(b+3)//2):
    print(' '*(b-c-i),'*'*(2*i-1))
