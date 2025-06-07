n = int(input ('inserire un numero intero positio maggiore di 1: '))
i=2
int(i)
while i<=n:
    m=1
    int(m)
    s=0
    while m<=i:
        if(i%m==0):
            s=s+1
        m+=1
    if (s==2):
        print(i)
        i+=1
