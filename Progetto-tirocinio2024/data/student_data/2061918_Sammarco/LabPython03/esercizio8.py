r=input("inserisci una stringa palindroma")
while r!=r[::-1]:
    r=input("Non è palindroma,inserisci una stringa palindroma")
print("stringa palindroma di lunghezza:",len(r))
