s = input("Inserire una stringa: ")
if s.islower() and s.isalpha():
    print(s[:1],s[len(s)-1:])
else:
    print(s[:1],s[len(s)-1:])
    while not (s.islower() and s.isalpha()):
        s = input("Inserire una stringa: ")
        if s.islower() and s.isalpha():
            print(s[:1],s[len(s)-1:])
            break
        else:
            print(s[:1],s[len(s)-1:])