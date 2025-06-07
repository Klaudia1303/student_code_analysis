s=input('inserire una stringa   ')
while len(s)==0:
    s=input('inserire una stringa non vuota  ')
while not s.isalpha() or not s.islower():
    print(str(s[0])+str(s[len(s)-1]))
    s=input('inserire una stringa   ')
    while len(s)==0:
        s=input('inserire una stringa non vuota  ')
print(str(s[0])+str(s[len(s)-1]))
