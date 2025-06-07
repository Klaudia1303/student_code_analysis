s = input('Inserisci una stringa: ')
dis = 0

for c in s:
    if s.rfind(c)-s.find(c) > 0:
        dis = s.rfind(c)-s.find(c)
print(dis)
