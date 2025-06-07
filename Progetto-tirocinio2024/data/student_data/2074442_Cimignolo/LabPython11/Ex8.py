import re

def placeZero(s):
    n = int(s)
    if n < 10:
        s = '0' + s
    return s

def Ex8(file):
    f = open(file, 'r', encoding='UTF-8')
    t = f.read().split('\n')
    f.close()
    l = []
    pattern = r'\b[A-Z]{6}([0-9][0-9])(\w)?([0-9][0-9])[A-Z][0-9]{3}[A-Z]\b'
    for r in t:
        s = re.search(pattern, r.replace(' ', ''))
        if s:
            a = s.group(1)
            m = s.group(2)
            d = int(s.group(3))
            if (int(a) <= 20):
                anno = '20' + a
            else:
                anno = '19' + a
            mesi = list('ABCDEHLMPRST')
            if (m in mesi):
                mese = str(mesi.index(m) + 1)
            else:
                l.append('Mese errato')
                continue
            if d > 40:
                d -= 40
            if (d < 32 and m != 'B') or (d < 29 and m == 'B'):
                giorno = str(d)
            else:
                l.append('Giorno errato')
                continue
            l.append(placeZero(giorno) + '/' + placeZero(mese) + '/' + anno)
        elif r != '':
            l.append('Codice errato')
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
