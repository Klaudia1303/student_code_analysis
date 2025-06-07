s=str(input('inserire una stringa: '))
carattere=''
for i in range(len(s)):
    conto=s.count(s[i])
if conto>=2:
    print(True)
else:
    print(False)
