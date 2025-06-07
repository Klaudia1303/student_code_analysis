n=str(input("Inserisci un numero: "))
count=0
while "*" not in n:
    n=int(input("Inserisci un altro numero: "))
    if n>0 and isinstance(n):
        count=count+1
print(count)