prec = input("Stringa: ")

while True:
    s = input("Stringa: ")
    if s[0] == prec[-1]:
        print(prec, s)
        break
    prec = s
