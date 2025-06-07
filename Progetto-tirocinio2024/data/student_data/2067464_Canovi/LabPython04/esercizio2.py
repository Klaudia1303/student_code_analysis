i = 0
n = 0
while i == 0:
    a = input("inserisci un numero intero ('*' per terminare): ")
    if a == "*":
        i = i + 1
    elif a != "*":
        a = int(a)
        if a >= 0:
            n = n + 1
print(n)
        
