s = input("Inserisci una stringa palindroma: ")
while s[:] != s[::-1]:
    s = input("non è palindroma,inserire una stringa palindroma: ")
if s[:] == s [::-1]:
    print("stringa palindroma di lunghezza "+str(len(s)))
