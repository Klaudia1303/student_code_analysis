s = input("Inserisci stringa: ")
count = 0
j = -1
for i in range(len(s)-1,-1,-1):
    j += 1
    if s[i] == s[j]:
        count += 1
    elif len(s[i]) == len(s[j]):
        break
print(count)
