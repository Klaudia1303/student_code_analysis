s=input("Inserire una stringa s: ")
s_piccolo=s.lower()
lunghezza=len(s_piccolo)
contalettera=0
for i in range(lunghezza):
    conta=s_piccolo.count(s_piccolo[i])
    if conta>=contalettera:
        lettera=s_piccolo[i]
        contalettera=conta
print(lettera +" " +str(contalettera))

