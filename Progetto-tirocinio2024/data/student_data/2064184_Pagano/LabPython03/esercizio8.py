last = input("Inserisci una stringa palindroma: ")

while last[:(len(last)//2)] != last[len(last):len(last)//2-1:-1]:
    last = input("Inserisci una stringa palindroma: ")

print("stringa palindroma di lunghezza " + str(len(last)))
