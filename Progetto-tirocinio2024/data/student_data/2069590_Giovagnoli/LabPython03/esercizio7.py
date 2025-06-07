c = input("Inserire un carattere: ")
boolean = True
while boolean:
    s = input("Inserire una stringa: ")
    if s.count(c)>2:
        print("Ci sono ",s.count(c)," ","\"",c,"\"")
        boolean = False
