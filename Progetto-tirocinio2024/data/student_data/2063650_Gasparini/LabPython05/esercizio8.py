b = int(input("Base: "))

max_y = (b - 1) // 2
for y in range(max_y + 1):
    spazi = " " * (max_y - y)
    print(spazi + "*" * (y * 2 + 1) + spazi)
