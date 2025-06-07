n1= int(input())
n2= int(input())

lista =[]


for n in range(n1+1):
    if n == 0:
        continue
    elif (n1%n)==0:           #e un suo divisore
        if n2%n != 0:       #controlla che n non sia divisore del secondo numero
            #print(n)
            n=int(n)
            lista.append(n)

    
newList = [num for num in reversed(lista)]
print(newList)
