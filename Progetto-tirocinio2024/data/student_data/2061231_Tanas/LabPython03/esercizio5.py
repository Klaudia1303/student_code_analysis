s = ''
while not (s.isalpha() and s.islower()):
    s = input("stringa: ")
    print(s[0]+s[-1])