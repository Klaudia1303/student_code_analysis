s = input("inserisci una stringa: ")
a = 0
for i in range(len(s)):
    if s.count(s[i]) > 1:
        a = 1
if a == 1:
    print("True")
else:   print("False")
