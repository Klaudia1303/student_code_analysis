def Ex8(file):
    f=open(file,'r',encoding='UTF-8')
    l=[]
    import re
    pattern=r'[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})([A-Z])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]'
    for riga in f:
        mese=['01','02','03','04','05','06','07','08''09','10','11','12']
        lettera=['A','B','C','D','E','H','L','M','P','R','S','T',]
        if re.match(pattern,riga):
            for i in range(12):
                if lettera[i]==riga[8]:
                    if int(riga[9:11])<=31:
                        if int(riga[6:8])>20:
                            l.append(riga[9:11]+str('/')+mese[i]+str('/')+str('19')+riga[9:11])
                        else:
                            l.append(riga[9:11]+str('/')+mese[i]+str('/')+str('20')+riga[9:11])
                    elif int(riga[9:11])>=40:
                        if int(riga[6:8])>20:
                            giorno=int(riga[9:11])-40
                            l.append(giorno+str('/')+mese[i]+str('/')+str('19')+riga[9:11])
                        else:
                            giorno=int(riga[9:11])-40
                            l.append(giorno+str('/')+mese[i]+str('/')+str('20')+riga[9:11])
                    else:
                        l.append('Giorno errato')
                else:
                    l.append('Mese errato')

        else:
            l.append('Codice errato')
    f.close()
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
