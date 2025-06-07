x=input("un carattere: ")
y=True

while y:
    z=input("una stringa: ")
    if z.count(x)>2:
        print(z.count(x))
        y=False
