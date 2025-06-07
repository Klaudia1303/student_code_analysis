n=float(input("inserisci l'eta del cane"))

if 0<n<=2:
    print(n*10.5)
elif n>2:
    print((2*10.5)+((n-2)*4))
else:
    print("eta non corretta")
