s1 = input("inserisci una stringa ")
s2 = input("inserisci una stringa ")
n = int(input("Inserisci un numero "))
for i in range(0, len(s1)):
    if s1[i] in s2:
        lettera = s2.find(s1[i])
        if (abs((lettera - i)) <= n or abs((i - lettera)) <= n):
            print(s1[i])
