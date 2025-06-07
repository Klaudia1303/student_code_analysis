s = input('inserisci una stringa: ')
a = 0
for i in s:
    b = s.rfind(i) - s.find(i)
    if (s.find(i) != s.rfind(i)) and a < b:
        a = b
print(a)

