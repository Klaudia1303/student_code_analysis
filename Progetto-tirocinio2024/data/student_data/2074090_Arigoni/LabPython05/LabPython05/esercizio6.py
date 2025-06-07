s=str(input("Inserisci una stringa>> "))
z=0

for i in range(len(s)):
    for n in range(len(s)):
        if s[i]==s[n]:
            if i-n>z:
                z=i-n
print(z)
