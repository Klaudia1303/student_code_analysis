

num = int(input('Inserire un numero: '))

if num > 1:
  
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "Non è un numero primo")
            break
        else:
            print(num, "E' un numero primo")
            break
else:
    print(num, "Non è un numero primo")