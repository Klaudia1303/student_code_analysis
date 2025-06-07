c = input('carattere: ')[0]
s = ''

while not (s.count(c) > 2):
    s = input('stringa: ')

print(s.count(c))
