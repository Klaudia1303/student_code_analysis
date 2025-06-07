num=int(input("Inserisci un numeratore: "))
den=int(input("Inserisci un denominatore: "))
if num<den:
    print("Frazione propria")
if num%den==0:
    print("Frazione apparente")
if num>den:
    print("Frazione impropria")