def Ex8(file):
    f = open(file, encoding = "UTF-8")
    l = []
    dmesi = {'A' : ['01', 31], 'B' : ['02', 28], 'C' : ['03', 31], 'D' : ['04', 30], 'E' : ['05', 31], 'H' : ['06', 30], 'L' : ['07', 31], 'M' : ['08', 31], 'P' : ['09', 30], 'R' : ['10', 31], 'S' : ['11', 30], 'T' : ['12', 31]}
    pattern = r'[A-Z]{3}\W*[A-Z]{3}\W*(\d)(\d)([A-Z])(\d)(\d)\W*([A-Z])\d{3}[A-Z]'
    for riga in f:
        m = re.search(pattern, riga)
        if m:
            if m.group(3) not in dmesi:
                l.append("Mese errato")
            else:
                giorno = int(m.group(4) + m.group(5))
                if giorno > 40:
                    giorno = giorno - 40
                if giorno > dmesi[m.group(3)][1]:
                    l.append("Giorno errato")
                else:
                    giorno = str(giorno)
                    if len(giorno) == 1:
                        giorno = "0" + giorno
                    anno = int(m.group(1) + m.group(2))
                    if anno <= 20:
                        anno = '20' + str(anno)
                    else:
                        anno = '19' + str(anno)
                    l.append(giorno + "/" + dmesi[m.group(3)][0] + "/" + anno)                        
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






