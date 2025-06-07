base=int(input("scrivi la base di un triangolo (maggiore di 3) : "))
if base >=3 and base%2 !=0:
    sott=0
    while sott<=(base/2-1):
        sott=sott+1
    n=0
    t=base-sott
    diminuire=0
    for i in range(1,t+1):
        spazio=" "*(t-diminuire)
        print(spazio,"*"*(i+n))
        n=n+1
        diminuire=diminuire+1

else:
    print("la base scelta è troppo piccola oppure è pari")
