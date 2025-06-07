s="input"
corretto=False
while not corretto:
    s=input("inserisci stringa palindroma")
    
    if s==s[::-1]:
        print("stringa palindroma di lunghezza "+str(len(s)))
        corretto=True
    else:
        print("non palindroma,inserire una stringa palindroma")
