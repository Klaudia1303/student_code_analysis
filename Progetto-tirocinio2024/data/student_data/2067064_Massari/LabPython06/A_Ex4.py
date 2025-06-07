PrimoViaggiatore=0
SecondoViaggiatore=0
for giorno in range(1,1001):
    PrimoViaggiatore+=20
    SecondoViaggiatore+=giorno
    if PrimoViaggiatore==SecondoViaggiatore:
        break
print(giorno)
