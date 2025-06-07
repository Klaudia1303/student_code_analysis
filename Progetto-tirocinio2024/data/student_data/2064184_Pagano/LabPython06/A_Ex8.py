s1 = input("Inserisci una stringa: ")
s2 = input("Inserisci una stringa: ")
n = int(input("Inserisci un numero intero: "))

result = ""

for i in range(len(s1)):
    if i-n >= len(s2):
        break

    minPos = max(i-n, 0)
    maxPos = min(i+n+1, len(s2))
    if s1[i] in s2[minPos:maxPos]:
        result += s1[i]

print(result)
