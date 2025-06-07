k=True
while k:
    n=int(input('Intero maggiore o uguale a 2 '))
    if n>=2:
        k=False
    else:
        print('Intero inserito minore di 2')
for i in range(n):
    if i==0 or i==n-1:
        print('*'*n)
    else:
        if i==0 or i==n-1:
            print('*'*n)
        if i<(n-1)/2:
            print('*',' '*int(i-1),'*',' '*int(n-((i*2)+2)),'*',' '*int(i-1),'*', sep='')
        elif i==(n-1)/2:
            print('*',' '*int(i-1),'*',' '*int(i-1),'*', sep='')
        else:
            print('*',' '*int(n-i-2),'*',' '*int(2*i-n),'*',' '*int(n-i-2),'*', sep='')
    
        
    
        
                          
