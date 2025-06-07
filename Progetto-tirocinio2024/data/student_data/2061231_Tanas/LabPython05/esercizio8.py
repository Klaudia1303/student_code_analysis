n = int(input("base triangolo isoscele: "))

for i in range(1, n+1, 2):
    spazi = ' '*((n-i)//2)
    print(spazi, '*'*i, spazi, sep='')
