anno = int(input("anno: "))
if (anno % 4 == 0 and not (anno % 100 == 0)) or (anno % 400 == 0):
    print("anno bisestile")
else:
    print("anno non bisestile")
