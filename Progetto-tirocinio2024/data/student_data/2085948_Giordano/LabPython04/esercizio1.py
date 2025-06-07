s=str(input("Inserisci una stringa: "))
count= 0
while "a" and "c" not in s:
    s=input("Inserisci una stringa: ")
    count = count+1
if "a" and "c" in s:
    print("Hai ripetuto l'inserimento della stringa", count,"volte")
