def Ex8(file):
    f = open(file,encoding="UTF-8")
    d = {'A':'01','B':'02','C':'03','D':'04','E':'05','H':'06','L':'07','M':'08','P':'09','R':'10','S':'11','T':'12'}
    pattern = r'[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})([A-Z])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]'
    mese30 = "DHPS"
    mese31 = "ACELMRT"
    mese28 = "B"
    a = f.readline()
    l = []
    while a != "":
        if re.match(pattern,a):
            anno = re.match(pattern,a).group(1)
            mese = re.match(pattern,a).group(2)
            giorno = int(re.match(pattern,a).group(3))
            s = ''
            if(giorno>=41 and giorno<=71):
                giorno -= 40
            if mese in mese28 :
                if giorno >= 1 and giorno <= 28:
                    s = s + str(giorno).zfill(2)+'/'+d.get(mese)+'/'
                    if int(anno) <= 20:
                        s = s + "20"+str(anno)
                    else:
                        s = s + "19"+str(anno)
                    l.append(s)
                else:
                    l.append("Giorno errato")
            elif mese in mese30:
                if giorno >= 1 and giorno <= 30:
                    s = s + str(giorno).zfill(2)+'/'+d.get(mese)+'/'
                    if int(anno) <= 20:
                        s = s + "20"+str(anno)
                    else:
                        s = s + "19"+str(anno)
                    l.append(s)
                else:
                    l.append("Giorno errato")
            elif mese in mese31:
                if giorno >= 1 and giorno <= 31:
                    s = s+str(giorno).zfill(2)+'/'+d.get(mese)+'/'
                    if int(anno) <= 20:
                        s = s+ "20"+str(anno)
                    else:
                        s = s+ "19"+str(anno)
                    l.append(s)
                else:
                    l.append("Giorno errato")
            else:
                l.append("Mese errato")
        else:
            l.append("Codice errato")
        a = f.readline()
    return l
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
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
