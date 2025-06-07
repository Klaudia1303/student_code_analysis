i = 0
while i == 0:
    s = input("inserisci una stringa palindroma: ")
    if s == s[::-1]:
        print("stringa palindroma di lunghezza", len(s))
        i = i + 1
    else: print("Non palindroma, inserire una stringa palindroma")
