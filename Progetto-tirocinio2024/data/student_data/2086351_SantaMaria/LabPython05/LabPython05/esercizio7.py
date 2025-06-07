s=input('Inserire una stringa: ')
comp=False
for i in range(len(s)):
    if s[i] in s[i+1:]:
        comp=True
print(comp)
