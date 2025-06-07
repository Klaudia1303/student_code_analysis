n = int(input('numero intero: '))
i=2
while i <= n:
    fine = True
    div=2
    while div < i:
        if i%div == 0:
            fine = False
        div = div+1
    if fine == True:
        print(i)
    i = i+1
