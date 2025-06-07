def Ex8(file):
    lista = []
    f = open (file, "r", encoding = "UTF-8")
    pattern = '[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})([A-Z])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]'
    testo = f.read()
    d = {'A':'01', 'B':'02', 'C':'03', 'D':'04', 'E':'05', 'H':'06', 'L':'07', 'M':'08', 'P':'09', 'R':'10', 'S':'11', 'T':'12'}
    i = re.finditer (pattern, testo)
    f.close()
    f = open (file, "r", encoding = "UTF-8")
    for riga in f:
        if re.match(pattern, riga):
            for elem in i:
                data = ''
                giorno = int()
                mese = ''
                anno = ''
                if int(elem.group(1)) <= 20:
                    anno = anno + '20' + str(elem.group(1))
                else:
                    anno = anno + '19' + str(elem.group(1))
                if int(elem.group(3)) >= 1 and int(elem.group(3)) <= 31:
                    if str(elem.group(2)) == 'B':
                        if int(elem.group(3)) > 28:
                            lista.append('Giorno errato')
                            #continue
                            break
                    else:
                        giorno = str(elem.group(3))
                elif int(elem.group(3)) >= 41 and int(elem.group(3)) <= 71:
                    giorno = int(elem.group(3)) - 40
                    if str(elem.group(2)) == 'B':
                        if int(elem.group(3)) > 28:
                            lista.append('Giorno errato')
                            #continue
                            break
                    else:
                        if giorno >= 10:
                            giorno = str(giorno)
                        else:
                            giorno = '0' + str(giorno)
                else:
                    lista.append('Giorno errato')
                    #continue
                    break
                if elem.group(2) in d:
                    mese = str(d[elem.group(2)])
                else:
                    lista.append('Mese errato')
                    #continue
                    break
                data = giorno + "/" + mese + "/" + anno
                lista.append(data)
                break
        else:
            lista.append('Codice errato')
            continue
    return lista

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
