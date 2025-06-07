def Ex8(file):
    date = []
    mesi = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "H": 6, "L": 7, "M": 8, "P": 9, "R": 10, "S": 11, "T": 12}

    with open(file, encoding='UTF-8') as f:
        for l in f:
            res = re.search(r"[A-Z]{3}\s*[A-Z]{3}\s*(\d{2})([A-Z])(\d{2})\s*[A-Z]\d{3}[A-Z]\b", l)
            if res:
                anno = 2000 + int(res.group(1)) if int(res.group(1)) < 20 else 1900 + int(res.group(1))

                if res.group(2) in mesi:
                    mese = mesi[res.group(2)]
                else:
                    date.append("Mese errato")
                    continue

                giorno = int(res.group(3))-40 if int(res.group(3)) > 40 else int(res.group(3))
                if (mese in [1,3,5,7,8,10,12] and giorno > 31) or \
                    (mese in [4,6,9,11] and giorno > 30) or \
                    (mese == 2 and giorno > 28):
                    date.append("Giorno errato")
                    continue

                date.append("{:02d}/{:02d}/{}".format(giorno, mese, anno))
            else:
                date.append("Codice errato")
    return date

    
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
