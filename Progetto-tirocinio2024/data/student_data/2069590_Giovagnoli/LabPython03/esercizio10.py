n = int(input("Inserire un numero intero positivo maggiore di 1: "))
if n<=1:
    print("Input non valido!!")
i = 2
x = 2
while i<=n:
    if i%x==0:
        if i==x:
            print(i)
            i+=1
        else:
            x+=1
    else:
        while i!=x:
            x+=1
            if i%x==0:
                i+=1
        print(i)
        i+=1