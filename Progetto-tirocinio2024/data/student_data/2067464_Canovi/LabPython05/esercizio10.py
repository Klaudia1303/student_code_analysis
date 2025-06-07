n = int(input("inserisci un numero positivo: "))
for i in range(n):
    s = ""
    for j in range(n):
        if i == j or (j + i) == (n - 1):
            s = s + "*"
        elif i == 0 or i == (n - 1):
            s = s + "*"
        elif j == 0 or j == (n - 1):
            s = s + "*"
        else:   s = s + " "
    print(s)        
