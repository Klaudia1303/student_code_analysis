s1 = input("inserisci una stringa ")
s2 = input("inserisci una stringa ")
n = int(input("Inserisci un numero "))
for c in range(0, len(s1)):
    if s1[c] in s2:
        lettera = s2.find(s1[c])
        if (abs((lettera - c)) <= n or abs((c - lettera)) <= n):
            print(s1[c])
