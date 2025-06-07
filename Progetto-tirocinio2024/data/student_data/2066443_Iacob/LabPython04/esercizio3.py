stop = False
n_int = 0
while not stop:
    n = input('Insert number (or * to stop): ')
    if n=='*':
        stop = True
    elif int(n)<=0:
        n_int = n_int + int(n)
print(n_int)
