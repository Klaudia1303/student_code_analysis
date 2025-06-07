print("questo programma stampa quante volte un caratte compare in una parola in cui compare più di 2 volte\n")
e=input("inserire il carattere")
i=0
while i==0:
    s=input("inserire una stringa")
    if s.count(e)>2:
        print(s.count(e))
        i+=1
