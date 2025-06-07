num=float(input("Inserisci il numeratore: "))
den=float(input("Inserisci il denominatore: "))
if num<den:
    print("Frazione propria")
if num%den==0:
    print("Frazione apparente")
if (num>den and not num%den==0):
    print("Frazione impropria")