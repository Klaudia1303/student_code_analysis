s = input("Inserisci una stringa: ")

mc = 0
ms = ""

for i in range(len(s)):
    count = s.count(s[i])
    if count >= mc:
        mc = count
        ms = s[i]

print(ms, mc)
