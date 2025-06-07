s1 = input("Inserisci una stringa: ")
s2 = input("Inserisci una stringa: ")

result = ""

for i in range(len(s1)):
    for j in range(len(s1), i, -1):
        _s = s1[i:j]
        if s2.find(_s) != -1:
            if len(_s) > len(result):
                result = _s
            break

print(result)
