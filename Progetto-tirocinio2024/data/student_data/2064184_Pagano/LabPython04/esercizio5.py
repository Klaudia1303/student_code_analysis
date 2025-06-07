num = int(input("Inserisci un intero maggiore o uguale a 0: "))

if num > 1:
    f = 1
    for i in range(2, num+1):
        f = f * i
    print(f)
elif num == 0 or num == 1:
    print(1)
else:
    print("Input non valido...")
