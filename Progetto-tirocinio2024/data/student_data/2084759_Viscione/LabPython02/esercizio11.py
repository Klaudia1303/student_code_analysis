t=int(input("immetti una temperatura sottoforma di intero: "))
if t>30:
    print("molto caldo")
elif t<=30 and t>20:
    print("caldo")
elif t<=20 and t>10:
    print("gradevole")
else:
    print("freddo")
