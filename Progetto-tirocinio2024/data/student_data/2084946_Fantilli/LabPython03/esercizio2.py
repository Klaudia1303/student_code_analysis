n = input()
n = int(n)
i = 1
while n%i == 0:
    print(i)
    i+=1
    while n%i != 0:
        i+=1
