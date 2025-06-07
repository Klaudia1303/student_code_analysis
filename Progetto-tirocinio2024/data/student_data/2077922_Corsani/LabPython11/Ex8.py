#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.8


def Ex8(file):
    a = open(file, encoding="UTF-8")
    x = a.readlines()
    a.close()
    l = []
    mesi = ["A", "B", "C", "D", "E", "H", "L", "M", "P", "R", "S", "T"]
    cf = r"^[A-Z]{3}\s*[A-Z]{3}\s*(\d{2})\s*([A-Z])\s*(\d{2})\s*[A-Z]\s*\d{3}\s*[A-Z]$"
    for r in x:
        m = re.search(cf, r)
        if m:
            r = r.replace(" ", "")
            yyyy, mm, dd = int(m.group(1)), m.group(2), int(m.group(3))
            #controllo anno
            if yyyy <= 20:
                yyyy += 2000
            else:
                yyyy += 1900
            #controllo mese
            if mm in mesi:
                mm = str(mesi.index(mm)+1).zfill(2)
            else:
                l.append("Mese errato")
                continue
            #controllo giorno
            if dd > 40:
                dd -= 40
            if dd > 31 or dd < 1 or (dd > 28 and mm == "02"):
                l.append("Giorno errato")
                continue
            #se arriva qui significa che la data è ben scritta
            l.append(str(dd).zfill(2)+"/"+mm+"/"+str(yyyy))
        else:
            l.append("Codice errato")
    return l

###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex8, ["codici1.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici2.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici3.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921'])
    counter_test_positivi += tester_fun(Ex8, ["codici4.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931'])
    counter_test_positivi += tester_fun(Ex8, ["codici5.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931', 'Codice errato', 'Giorno errato'])

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
