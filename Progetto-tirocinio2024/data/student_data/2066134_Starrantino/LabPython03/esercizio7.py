c: str = input('char: ')


index: int = 0

while True:
    s = input('> ')
    if s.count(c) > 2:
        print(s.count(c))
        break
    index += 1

