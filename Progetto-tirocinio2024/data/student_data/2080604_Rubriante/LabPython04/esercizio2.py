n=input("Inserisci un numero poitivo o negativo: ")
count=0
while n!="*":
    if n[0]!="-":
        count+=1
    n=input("Inserisci un numero poitivo o negativo: ")
print(count)
