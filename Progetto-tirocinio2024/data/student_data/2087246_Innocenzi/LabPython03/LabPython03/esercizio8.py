s=input("Inserisci una stringa palindroma: ")

if(s[:]!=s[::-1]):
    print("Non palindroma")
elif((s[:]==s[::-1])):
    print("Stringa palindroma di lunghezza", len(s))

while(s[:]!=s[::-1]):
    s=input("Inserisci una stringa palindroma: ")
    
    if(s[:]!=s[::-1]):
        print("Non palindroma")
    elif(s[:]==s[::-1]):
        print("Stringa palindroma di lunghezza", len(s))

