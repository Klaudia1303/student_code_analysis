s=input('inserire una stringa   ')
M=0
c=''
for i in range(len(s)):
    if s.rfind(s[i])-i>M:
        M=s.rfind(s[i])-i
        c=s[i]
print('il carattere ripetuto è',c,'distanziato',M)
