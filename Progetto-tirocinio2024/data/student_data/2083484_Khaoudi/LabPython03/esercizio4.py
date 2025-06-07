x=int(input("Inserisci x: "))
y=int(input("Inserisci y: "))

while x<0 or x>10:
     x=int(input("Inserisci x: "))

while y<0 or y>10:
    y=int(input("Inserisci y: "))

i=0
while i<=10:
    if i!=x and i!=y:
        print(i)
    i+=1;
