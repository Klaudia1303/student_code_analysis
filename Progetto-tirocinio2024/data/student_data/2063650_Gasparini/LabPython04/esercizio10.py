prec_1 = input("Stringa: ")
prec_2 = input("Stringa: ")

while True:
    s = input("Stringa: ")
    if len(s) == len(prec_1) + len(prec_2):
        print(prec_1, prec_2, s)
        break
    prec_1 = prec_2
    prec_2 = s
