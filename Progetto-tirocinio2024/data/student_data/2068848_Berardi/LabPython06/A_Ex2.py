s = input("inserisci la stringa: ")
lvl = 0
for i in range(len(s)//2):
    if s[i] == s[len(s)-i-1]:
        lvl += 1
if lvl == len(s)//2:
    print("palindroma")
else:
    print("livello",lvl)