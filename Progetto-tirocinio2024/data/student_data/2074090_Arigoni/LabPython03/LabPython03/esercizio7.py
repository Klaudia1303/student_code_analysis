stop=True
i=input("Inserisci un carattere")
while stop:
    s=input("Inserisci una stringa")
    if s.count(i)>2:
        print(s
              .count(i))
        stop=False
