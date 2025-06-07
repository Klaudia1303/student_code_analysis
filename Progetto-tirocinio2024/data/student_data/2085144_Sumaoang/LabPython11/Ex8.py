mese = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'H': 6,
    'L': 7,
    'M': 8,
    'P': 9,
    'R': 10,
    'S': 11,
    'T': 12
}

giorno = {
    'A': 31,
    'B': 28,
    'C': 31,
    'D': 30,
    'E': 31,
    'H': 30,
    'L': 31,
    'M': 31,
    'P': 30,
    'R': 31,
    'S': 30,
    'T': 31
}

def Ex8(file):
    data = []
    f = open(file, encoding="UTF-8")
    r = r"\b[A-Z]{3} *[A-Z]{3} *([0-9]{2})([A-Z])([0-9]{2}) *[A-Z][0-9]{3}[A-Z]\b"
    
    for x in f:
        y = re.match(r, x)
        if not y is None:
            anno = int(y.group(1))
            anno += 2000 if anno <= 20 else 1900        
            g = int(y.group(3))
            g -= 40 if g > 40 else 0
            m = y.group(2)
            limite_giorno = giorno.get(m, 0)      

            if limite_giorno != 0:
                if g <= limite_giorno:
                    data.append(f"{g:02d}/{mese[m]:02d}/{anno}")
                else:
                    data.append('Giorno errato')
            else:
                data.append('Mese errato')
        else:
            data.append('Codice errato')

    return data

        
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
