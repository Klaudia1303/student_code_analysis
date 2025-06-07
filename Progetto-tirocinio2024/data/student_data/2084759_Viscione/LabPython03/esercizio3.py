divisibile=False
print("andro' avanti finche' non immetterai un numero divisibile per 5")
while not divisibile:
    n=int(input("immetti un intero: "))
    if n%5==0:
        divisibile=True
        print(n//5)
