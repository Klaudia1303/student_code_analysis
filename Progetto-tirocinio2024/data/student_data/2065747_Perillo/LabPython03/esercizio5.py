s=input("inserire una stringa ")
while not s.isalpha() or not s.islower():
    print(s[0]+s[-1])
    s=input("inserire una stringa ")
print(s[0]+s[-1])
