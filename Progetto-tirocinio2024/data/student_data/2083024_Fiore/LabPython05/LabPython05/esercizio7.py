s = input("inserisc una stringa per vede se c'è un lettera che compare più volte: ")
stato = False
for i in range(len(s)):
    for v in range(i+1,len(s)):
        if s[i] == s[v]:
            stato = True

print(stato)
