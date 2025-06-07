corretto=False
while not corretto:
    s=str(input("Inserisci stringa palindroma "))
    x=s[0:len(s)]
    y=s[::-1]
    if x!=y:
        print("non palindroma, inserire una stringa palindroma")
        corretto=False
    else:
        print("Stringa palindroma di lunghezza",len(s))
        corretto=True
