s=input("inserisci stringa")
y=True
while y:
    if s==s[::-1]:
        l=len(s)
        print("palindroma",l)
        break
    else:
        s=input("non palindroma, inserisci nuova stringa")
        
