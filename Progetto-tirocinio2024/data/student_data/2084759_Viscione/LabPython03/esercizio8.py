palindroma=False
while not palindroma:
    s=input("Immetti una stringa: ")
    if s==s[::-1]:
        palindroma=True
        print("stringa palindroma di lunghezza", len(s))
    else:
        print("non palindroma, inserire una stringa palindroma")
