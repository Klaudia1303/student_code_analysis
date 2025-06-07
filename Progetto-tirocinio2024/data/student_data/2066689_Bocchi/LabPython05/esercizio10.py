l= int(input('lato quadrato: '))
p='*'
s=' '
x=l
sa=0
sc=l-4
volte= l/2
volte= int(volte)

print(p*l)
for i in range(volte-1):
    print(p+ s*sa +p+ s*sc +p +s*sa +p)
    x= x-1
    sa= sa+1
    sc= sc-2
if l%2 == 1:
    print(p+ s*sa +p+ s*sc +s*sa +p)
x= x+1
sa= sa-1
sc= sc+2
for i in range(volte-1):
    print(p+ s*sa +p+ s*sc +p +s*sa +p)
    x= x+1
    sa= sa-1
    sc= sc+2
print(p*l)
