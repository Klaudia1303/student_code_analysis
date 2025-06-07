n = int(input("inserisci un lato di un quadrato: "))

spazio= n-2
for i in range(n):
    if i < 1 or i == n-1:
        print("*" * n)
    else:
        print("*", " "*spazio, "*" ,sep = "")
