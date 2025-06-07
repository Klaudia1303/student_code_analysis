s=input("inserisci stringa: ")
check=False
for i in range(len(s)):
    if s[i] in s[i+1::]:
        check=True
print('ci sono caratteri che si ripetono? ', check)

