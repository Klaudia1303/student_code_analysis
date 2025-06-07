n: int = int(input('n > 1: '))

count: int = 2

while count <= n:
    l: int = 2

    while l <= count//2:
        if count % l == 0:
            break
        l += 1

    else: 
        print(count)

    count += 1
