s=str(input("Inserire una stringa:"))
b=True
while b:
    print(s[0]+s[len(s)-1])
    s=str(input("Inserire un'altra stringa:"))
    if s.isalpha() and s.islower():
        b=False

