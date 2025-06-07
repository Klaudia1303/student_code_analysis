def Ex8(file):
    pattern='[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})([A-Z])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]'
    fin = open(file)
    l = []
    mesi = 'ABCDEHLMPRST'
    for riga in fin:
        codice=re.match(pattern,riga)
        if  codice:
            cf = codice.group(0)
            giorno = int(codice.group(3))
            mese = codice.group(2)
            anno = int(codice.group(1))
            if mese in mesi:
                m=mesi.find(mese)+1
                if m<10:
                    m='0'+str(m)
                else:
                    m=str(m)

                if anno>20:
                    a='19'+str(anno)
                else:
                    a='20'+str(anno)

                if giorno<10 or 40<giorno<50:
                    g='0'+str(giorno)
                else:
                    g=str(giorno)
                    
                if mese in 'DHPS':
                    if (1 <= giorno <= 30) or (41 <= giorno <= 70):
                        if giorno < 40:
                            if giorno < 10:
                                l.append('0'+str(giorno)+'/'+m+'/'+a)
                            else:
                                l.append(str(giorno)+'/'+m+'/'+a)
                        else:
                            if giorno < 50:
                                l.append('0'+str(giorno-40)+'/'+m+'/'+a)
                            else:
                                l.append(str(giorno-40)+'/'+m+'/'+a)
                    else:
                        l.append('Giorno errato')
                elif mese=='B':
                    if (1 <= giorno <= 28) or (41 <= giorno <= 68):
                        if giorno < 40:
                            if giorno < 10:
                                l.append('0'+str(giorno)+'/'+m+'/'+a)
                            else:
                                l.append(str(giorno)+'/'+m+'/'+a)
                        else:
                            if giorno < 50:
                                l.append('0'+str(giorno-40)+'/'+m+'/'+a)
                            else:
                                l.append(str(giorno-40)+'/'+m+'/'+a)
                    else:
                        l.append('Giorno errato')
                else:
                    if (1 <= giorno <= 31) or (41 <= giorno <= 71):
                        if giorno < 40:
                            if giorno < 10:
                                l.append('0'+str(giorno)+'/'+m+'/'+a)
                            else:
                                l.append(str(giorno)+'/'+m+'/'+a)
                        else:
                            if giorno < 50:
                                l.append('0'+str(giorno-40)+'/'+m+'/'+a)
                            else:
                                l.append(str(giorno-40)+'/'+m+'/'+a)
                    else:
                        l.append('Giorno errato')

            else:
                l.append('Mese errato')

        else:
            l.append('Codice errato')
        
    fin.close()
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
