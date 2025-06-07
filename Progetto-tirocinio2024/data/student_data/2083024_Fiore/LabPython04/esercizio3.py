s = input("Inserisci dei numeri per fare la somma di tutti i numeri negativi inseriti. (* per terminare): ")
neg = 0
while s != "*":
    num = int(s)
    if num < 0:
        
        neg += num
    s = input("Inserisci dei numeri per fare la somma di tutti i numeri negativi inseriti. (* per terminare): ")

print(neg)
