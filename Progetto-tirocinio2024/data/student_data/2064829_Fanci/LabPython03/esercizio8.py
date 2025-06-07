while True:
    s = input("inserisci stringa palindroma: ")
    if str(s)== str(s)[::-1]:
        print("stringa palindroma di lunghezza: ",len(s))
        break
    print("stringa non palindroma")
