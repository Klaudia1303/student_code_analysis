s=input("Inserire una stringa:  ")
a=False
while a==False:
    print(s[0],s[len(s)-1])
    if s.isalpha() and s.islower():
        a=True
    else:
        a=False
        s=input("Inserire una stringa:  ")
