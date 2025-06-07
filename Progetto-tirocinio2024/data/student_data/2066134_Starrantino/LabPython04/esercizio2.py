s = ''
count: int = 0
while s != '*':
    s = input('numero: ')
    if s.isdecimal():
        count += 1
        
print(count)