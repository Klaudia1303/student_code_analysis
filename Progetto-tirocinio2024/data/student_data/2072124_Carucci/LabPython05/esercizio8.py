b = int(input('Base di un triangolo isoscele (intero dispari maggiore o uguale a 3): '))

j = b//2
for i in range(1, b+1, 2):
    print((' '*j)+('*'*i))
    j-=1
