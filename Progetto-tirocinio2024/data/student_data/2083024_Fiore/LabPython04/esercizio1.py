c = True
counter = 0
while c:
    s = input("inserisci una stringa (il programma termina quando inserisci una stinga che contiene 'c' e 'a'): ")
    n = 0
    counter += 1
    var = ""
    counter_a = 0
    counter_c = 0
    while n < len(s):
        if counter_c == 1 and counter_a == 1:
            print(counter)
            c = false
        elif s[n].lower() == "a" and counter_a == 0:
            var = var +"a"
            counter_a += 1
            n +=1
        elif s[n].lower() == "c" and counter_c == 0:
            var = var +"c"
            counter_c += 1
            n += 1
        if counter_c == 1 and counter_a == 1:
            print(counter)
            c = False
        else:
            n += 1
