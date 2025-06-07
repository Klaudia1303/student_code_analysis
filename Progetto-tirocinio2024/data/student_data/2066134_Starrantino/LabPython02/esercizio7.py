n = int(input('n: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))

numbers = [n, n2, n3]
for _ in range(len(numbers)):
    mx = max(numbers)
    print(mx)
    numbers.remove(mx)
