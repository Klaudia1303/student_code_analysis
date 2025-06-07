n: int = 0
s: str = ''
while s != '*':
    s = input('numero: ')
    if s.replace('-', '').isnumeric():
        num: int = int(s)
        if num < 0:
            n += num
print(n)