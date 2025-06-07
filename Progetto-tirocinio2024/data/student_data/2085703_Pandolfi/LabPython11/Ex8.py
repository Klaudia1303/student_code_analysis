def Ex8(file):
    f = open(file, "r", encoding="UTF-8")
    riga = "1"

    lista = []

    d_mesi = {"A" : "01", "B" : '02', "C" : "03", "D" : "04", "E" : "05", "H" : "06", 
    "L" : "07", "M" : "08", "P" : "09", "R" : "10", "S" : "11", "T" : "12"}
    d_giorni_mesi = {"A" : 31, "B" : 28, "C" : 31, "D" : 30, "E" : 31, "H" : 30, 
    "L" : 31, "M" : 31, "P" : 30, "R" : 31, "S" : 30, "T" : 31}    

    pattern_cdf = r"\b[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]\b"
    pattern_gg = r"\d{2}"


    while riga != "":
        riga = f.readline()
        if riga == "":
            break
        riga = riga.replace(" ", "")
        if re.search(pattern_cdf, riga):
            if riga[8] not in d_mesi:
                lista.append("Mese errato")
                continue
            m = re.findall(pattern_gg, riga)
            if (d_giorni_mesi[riga[8]] < int(m[1]) and int(m[1]) < 40) | (int(m[1]) > 40 and d_giorni_mesi[riga[8]] < int(m[1]) - 40) | (int(m[1]) - 40 == 0):
                lista.append("Giorno errato")
                continue
            else: 
                giorno = 0
                anno = 0
                if int(m[1]) < 40:
                    giorno = int(m[1])
                    print(giorno)
                else: 
                    giorno = int(m[1]) - 40
                if int(m[0]) <= 20:
                    anno = 2000 + int(m[0])
                else:
                    anno = 1900 + int(m[0])
                lista.append(str(giorno).zfill(2) + "/" + d_mesi[riga[8]] + "/" + str(anno))
        else:
            lista.append("Codice errato")   

    f.close()

    return lista

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
