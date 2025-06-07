s = input("Inserisci una stringa: ")
i = 0
char = 0
while i < len(s):
        if s.count(s[i]) >= char:
            char = s.count(s[i])
            ps = i
        i = i+1
print(s[ps])
