def Ex8(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    fin=open(file, encoding="UTF-8")
    lista=[]
    nummesi={"A":"01","B":"02","C":"03","D":"04","E":"05","H":"06","L":"07","M":"08","P":"09","R":"10","S":"11","T":"12"}
    giornimesi={"A":31,"B":28,"C":31,"D":30,"E":31,"H":30,"L":31,"M":31,"P":30,"R":31,"S":30,"T":31}
    for r in fin:
        codice=re.search(r"[A-Z]{3}\s*[A-Z]{3}\s*([0-9][0-9])([A-Z])([0-9][0-9])\s*[A-Z][0-9]{3}[A-Z]",r)
        if codice:
            anno=codice.group(1)
            mese=codice.group(2)
            giorno=int(codice.group(3))
            if mese in nummesi:
                if ((1<=giorno<=giornimesi[mese]) or (40<giorno<=giornimesi[mese]+40)):
                    if int(anno)<=20:
                        anno="20"+anno
                    else:
                        anno="19"+anno
                    if giorno>40:
                        giorno=giorno-40
                        if giorno<10:
                            giorno="0"+str(giorno)
                    lista.append(str(giorno)+"/"+nummesi[mese]+"/"+anno)
                else:
                    lista.append("Giorno errato")
            else:
                lista.append("Mese errato")
        else:
            lista.append("Codice errato")
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
