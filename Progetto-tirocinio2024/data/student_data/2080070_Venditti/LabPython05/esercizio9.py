s=int(input('inserire un intero dispari maggiore o uguale a 3: '))
n= s-2
for i in range(1,s+1):
    if i==1 or i==s:
        print(s*'*')
    else:
        print('*'+' '*n+'*')
    
    
