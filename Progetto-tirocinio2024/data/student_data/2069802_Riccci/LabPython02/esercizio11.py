t = int(input("Inserisci valore temperatura --> "))
if(t>30):
    print("molto caldo")
elif(t>20 and t<30):
    print("caldo")
elif(t>10 and t<20):
    print("gradevole")
else:
    print("freddo")
