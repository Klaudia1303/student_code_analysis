print("ESERCIZIO 6: inserimento del numeratore e di un denominatore \
e dice se risulta propria, impropria o apparente\n")
n=int(input("Inserire il numeratore di una frazione: \t"))
d=int(input("Inserire il denominatore di una frazione: \t"))
if n<d:
    print("Propria")
elif n>d:
    print("Impropria")
elif n%d==0:
    print("Apparente")
