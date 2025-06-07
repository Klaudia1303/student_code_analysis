s = input("Inserisci stringa: ")
t0 = 0
if len(s)!=0:

    t0 = s.count(s[0])

    for i in s[1]:

        

        t = s.count(i)

        if t>t0:
            t=t


    print(i, t)

        

else:
    print("Stringa non valida")
