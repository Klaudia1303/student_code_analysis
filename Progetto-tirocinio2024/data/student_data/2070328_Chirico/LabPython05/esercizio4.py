n_1 = int(input('numero intero = '))
n_2 = int(input('altro numero intero più grande = '))

for i in range(n_1,n_2+1):
    if i < n_2 and i%n_1 == 0:
        print(i)
