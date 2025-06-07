s = input("inserisci una stringa: ")
n = int(input("inserisci un numero: "))
for i in range (len(s)):
    if s.rfind(s[i]) - s.find(s[i])== n :
        print(True)
        break
if s.rfind(s[i]) - s.find(s[i])!= n:
    print(False)

