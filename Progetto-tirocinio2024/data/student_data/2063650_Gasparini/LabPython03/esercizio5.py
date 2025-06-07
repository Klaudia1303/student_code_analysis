finito = False
while not finito:
    s = input("Stringa: ")
    print(s[0] + s[-1])
    finito = s.islower() and s.isalpha()
