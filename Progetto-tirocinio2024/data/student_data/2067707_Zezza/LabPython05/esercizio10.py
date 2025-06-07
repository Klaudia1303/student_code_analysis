l=int(input('lato intero: '))
n=0
k=4
i=0
stop=1
while i<=(l-1):
    if i==0 or i==l-1:
        print('*'*l)
        i+=1
    else:
        while i<(l/2)-1:
            print('*'+n*' '+'*'+(l-k)*' '+'*'+n*' '+'*')
            k+=2
            n+=1
            i+=1
        if l%2!=0:
            print('*'+int((l-3)/2)*' '+'*'+int((l-3)/2)*' '+'*')
            i+=1
        else:
            print('*'+int((l-4)/2)*' '+'**'+int((l-4)/2)*' '+'*')
            print('*'+int((l-4)/2)*' '+'**'+int((l-4)/2)*' '+'*') 
            i+=1
        while i>=l/2 and i<l-1:
            if i==(l-2) and l%2==0:
                print('*'*l)
                i+=1
                stop=0
            k-=2
            n-=1
            i+=1
            if stop!=0:
                print('*'+n*' '+'*'+(l-k)*' '+'*'+n*' '+'*')

            
