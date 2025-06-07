s=input('inserisci una stringa: ')
finito=False
for i in range(len(s)):
    if s.find(s[i])!=s.rfind(s[i]):
        while not finito:
            print(True)
            finito=True
if s.find(s[i])==s.rfind(s[i]):
    print(False)
