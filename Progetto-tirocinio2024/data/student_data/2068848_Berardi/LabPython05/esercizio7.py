s = input("inserisci una stringa: ")
temp = False
for i in s:
    if s.count(i)>1:
        temp = True
print(temp)