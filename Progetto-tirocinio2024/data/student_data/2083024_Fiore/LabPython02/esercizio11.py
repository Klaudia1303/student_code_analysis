t = int(input("inserisci la temperatura sotto forma di numero inteno: "))

if t > 30:
    print("molto caldo")
elif t > 20 and t <= 30:
    print("caldo")
elif t > 10 and t <= 20:
    print("gradevole")
elif t <= 10:
    print("freddo")
