o="" #primo modo
for i in range(1,11):
    for j in range(1,11):
        p=i*j
        while(p!=0):
            r=p%8
            p=p//8
            o=str(r)+o
        print(o,end=" ")
        o=""
    print()

s=''  #secondo modo
for i in range(1,11):
    for i in range(1,11):
        p=i*j
        while p!=0:
            r=p%8
            p=p//8
            s+=str(r)
        print(s[::-1],end='\t')
        s=''
    print('\n')
            
