n=input("Inserire un numero intero (* per terminare): ")
p=0
while n!='*':
    n=int(n)
    if n>=0:
        p+=1
    n=input("Inserire un numero intero (* per terminare): ")
print(p)
