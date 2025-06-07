print("Immetti due interi compresi nell'intervallo [0,10]")
x=int(input("Immetti x: "))
y=int(input("Immetti y: "))
i=0
while i<=10:
    if i != x and i != y:
        print(i)
    i+=1
