n = int(input("Inserire un numero intero maggiore di zero:"))
d = 1
while d <= n:
    if n%d == 0:
        print(d)
    d = d+1
        
