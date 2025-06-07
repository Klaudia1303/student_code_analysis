b = int(input("inserisci valore della base: "))
h = (b-1)//2
for i in range (1,b+1,2):
    if h >= 0:
        print(" "*h,"*"*i)
        h -= 1

print()
