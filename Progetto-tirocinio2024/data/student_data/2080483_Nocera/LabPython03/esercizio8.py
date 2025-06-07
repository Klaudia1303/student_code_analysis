i = 0
while i == 0:
    s = str(input("inserisci una parola palindroma : "))
    contrario = s[-1:-len(s)-1:-1]
    giusta = s[0:len(s)+1]
    if giusta == contrario:
        print("stringa palindroma di lunghezza "+str(len(giusta)))
        i = 1
    else: print("non palindroma, inserire una stringa palindroma")
