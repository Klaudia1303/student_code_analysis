#jade=lettera che sta venendo analizzate(possibile nuovo massimo)
#Se alla variabile "codiceUnicode" si inserisce lo "0",
#e all'ultima condizione "if" si inserisce "codiceUnicode>1114112",
#verrà effettuata una verifica della stringa con tutto il codiceUnicode.

s=str(input("Inserire una stringa:"))
codiceUnicode=ord("A")
controlloPrecedente=0
posizionePrecedente=0
massimo=0
b=True
while b:
    jade=s.count(chr(codiceUnicode))
    posizioneJade=s.rfind(chr(codiceUnicode))
    if jade<controlloPrecedente:
        massimo=massimo
    if jade==controlloPrecedente:
        if posizioneJade>posizionePrecedente:
            massimo=chr(codiceUnicode)
        else:
            massimo=massimo
    if jade>controlloPrecedente:
        massimo=chr(codiceUnicode)
        posizionePrecedente=s.rfind(chr(codiceUnicode))
        controlloPrecedente=jade
    if codiceUnicode>122:
        b=False
        print(massimo)
    codiceUnicode=codiceUnicode+1
        

    
        
        
