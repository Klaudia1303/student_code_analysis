s=input("Inserisci una stringa plindroma: ")
while s!=s[::-1]:
    print("Non palindroma, inserire una stringa palindroma:")
    s=input("Inserisci una stringa plindroma: ")
print("Stringa palindroma di lunghezza",len(s))
