s = input("Inserisci una stringa: ")
n = int(input("Inserisci un numero: "))
same_char = False
for i in range(len(s)-n):
    if s[i] == s[i+n]:
        same_char = True
print(same_char)
