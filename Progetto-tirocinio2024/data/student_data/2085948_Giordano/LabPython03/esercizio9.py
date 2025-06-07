num = int(input("Inserisci un numero: "))
for i in range(2,num+1):
    if (num % i) == 0:
            print(num, "non è un numero primo")
            break
    else:
        print(num, "è un numero primo")
        break
else:
    print(num, "non è un numero primo")