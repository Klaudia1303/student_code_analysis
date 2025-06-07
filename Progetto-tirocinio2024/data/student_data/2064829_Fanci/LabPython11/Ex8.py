def Ex8(file):
    f=open(file,encoding="UTF-8")
    l=[]
    pattern=r'[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})([A-Z])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]'
    mesi='ABCDEHLMPRST'
    for line in f:
        if re.match(pattern,line):
            m=re.search(pattern,line)
            i=re.finditer(pattern,line)
            for m in i:
                mese=m.group(2)
                giorno=int(m.group(3))
                anno=int(m.group(1))
                if mese in mesi:
                    mese = mesi.find(mese)+1
                    mese=str(mese)
                    if len(mese)==1:
                        mese='0'+mese
                    if 0<giorno<32 or 40<giorno<72:
                        if 40<giorno<72:
                            giorno=giorno-40
                    else:
                        l.append('Giorno errato')
                else:
                    l.append('Mese errato')
                if giorno>28 and mese=='02':
                    l.append('Giorno errato')
                else:
                    giorno=giorno
                if giorno==31 and (mese=='11' or mese=='09' or mese=='04' or mese=='06'):
                    l.append('Giorno errato')
                else:
                    giorno=giorno
                if anno>20:
                    anno=1900+anno
                else:
                    anno=2000+anno
        else:
            l.append('Codice errato')
        l.append(str(giorno)+'/'+str(mese)+'/'+str(anno))
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
