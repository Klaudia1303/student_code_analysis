n = int(input('inserisci un numero diverso da 1: '))
div = 2
count = 0

while div<=(n/2) and count==0:
    if n%div == 0:
        count+=1
        div+=1
if count==0:
        print(n)
n-=1





        
