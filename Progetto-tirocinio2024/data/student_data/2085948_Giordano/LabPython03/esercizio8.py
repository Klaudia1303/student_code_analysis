s=str(input("Inserisci una stringa palindroma: "))
while s!=s[::-1]:
    s=str(input("TI HO CHIESTO UNA STRINGA PALINDROMA: "))
else:
    x=len(s)
    print("Stringa palindroma di lunghezza ",x)