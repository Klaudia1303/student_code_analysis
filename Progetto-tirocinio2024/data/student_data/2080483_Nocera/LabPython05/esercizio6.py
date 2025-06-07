s=input("scrivi una parola :")
if s!="":
    maxcar=0
    for i in range(len(s)):
        car=s[i]
        doppia=s.rfind(car)
        distanza=doppia-i
        maxcar=max(distanza,maxcar)

    print(maxcar)        
        

else:
    print("la stringa è vuota")
