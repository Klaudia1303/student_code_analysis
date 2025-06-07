stop = False
n_int = 0
while not stop:
    n = int(input('Insert number (or 0 to stop): '))
    if n==0:
        stop = True
    elif n%3==0:
        n_int = n_int + n
print(n_int)
