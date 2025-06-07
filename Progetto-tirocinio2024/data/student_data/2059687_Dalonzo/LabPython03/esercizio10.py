
n = int(input('Inserie un numero positivo maggiore di 2: '))
count = 2

while(count <= n):
    num = count
    for i in range(2, num):
        if (num % i) != 0:
            print(num, "E' un numero primo")
            break
        else:
            break
    count += 1