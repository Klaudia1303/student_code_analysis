s = input("inserisci una stringa: ")
n = 0
car = ""
counter = 0
while n < len(s) and s != "":
    c = s[n]
    con = 0
    pos = 0
    while pos < len(s):
        if s[n] == s[pos]:
            con += 1
        if con >= counter:
            counter = con
            car = c
        pos += 1
    n += 1
            
print(car)
if s == "":
    print("devi inserire una stringa")
