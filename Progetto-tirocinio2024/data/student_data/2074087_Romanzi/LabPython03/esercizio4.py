c=True
while c:
    x=int(input('Numero intero x '))
    y=int(input('Numero intero y '))
    if x>=0 and x<=10 and y<=10 and y>=0:
        c=False
l=0
while l<=10:
    if x!=l and y!=l:
        print(str(l))
        l=l+1
    else:
        l=l+1
    
