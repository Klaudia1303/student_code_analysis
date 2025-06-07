t=float(input("Inserisci una temperatura: "))

if(30<t):
    print("Molto caldo")
elif(t<=30 and 20<t):
    print("Caldo")
elif(t<=20 and 10<t):
    print("Gradevole")
elif(t<=10):
    print("Molto freddo")