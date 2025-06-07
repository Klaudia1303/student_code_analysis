s=" "
corretto=s.isalpha()
corretto1=s.islower()
while not (corretto and corretto1):
    s=input("Inserisci una stringa: ")
    corretto=s.isalpha()
    corretto1=s.islower()
    print(s[0]+""+s[-1])
    
