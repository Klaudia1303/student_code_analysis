s = input('inserisci una stringa: ')
for i in range(len(s)):
    if s.find(s[i])!=s.rfind(s[i]):
              print(s.rfind(s[i]))
              break
