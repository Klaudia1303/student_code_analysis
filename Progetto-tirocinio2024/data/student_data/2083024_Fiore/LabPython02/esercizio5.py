anno = int(input("inserisci un anno per verificre se è bisestile: "))

if (anno % 4) == 0 and anno / 100 != 0:
    print("anno bisestile")

else:
    print("anno non bisestile")
