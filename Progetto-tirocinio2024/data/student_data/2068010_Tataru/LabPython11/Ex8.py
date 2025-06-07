def Ex8(file):
    import re
    me=['A','B','C','D','E','H','L','M','P','R','S','T']
    l=[]
    f = open(file,encoding="UTF-8")
    fr=f.read()
    for elem in '.,;:!?<>"-«»()\' ':
        fr=fr.replace(elem,"")
    fr=fr.split()
    for el in fr:
        rm=0
        rg=0
        m=re.search(r'\b[A-Z]{6}\d\d\w\d\d\w\d{3}\w\b',el)
        if m:
            for i in range(len(me)):
                if me[i]==el[8]:
                    rm=i+1
            if rm==0:
                l.append('Mese errato')
                continue
            else:
                g=int(el[9]+el[10])
                #febbraio m
                if rm==2 and g<28:
                    rg=g
                    return rg,l[i]
                #febbraio f
                elif rm==2 and (g>40 and g<69):
                    rg=g-40
                    return rg,l[i]
                #gen\mar\mag\lug m
                elif rm<8 and rm%2!=0 and g<32 and rm!=2:
                    rg=g
                #gen\mar\mag\lug f
                elif rm<8 and rm%2!=0 and (g>40 and g<72) and rm!=2:
                    rg=g-40
                #apr\giu m
                elif rm<8 and rm%2==0 and g<31 and rm!=2:
                    rg=g
                #apr\giu f
                elif rm<8 and rm%2==0 and (g>40 and g<71) and rm!=2:
                    rg=g-40
                #ago\ott\dic m
                elif rm>7 and rm<13 and rm%2==0 and g<32 and rm!=2:
                    rg=g
                #ago\ott\dic f
                elif rm>7 and rm<13 and rm%2==0 and (g>40 and g<72) and rm!=2:
                    rg=g-40
                #set\nov m
                elif rm>7 and rm<13 and rm%2!=0 and g<31 and rm!=2:
                    rg=g
                #set\nov f
                elif rm>7 and rm<13 and rm%2!=0 and (g>40 and g<71) and rm!=2:
                    rg=g-40
                else:
                    l.append('Giorno errato')
                    continue
                if (rm<10):
                    rm='0'+str(rm)
                if (rg<10):
                    rg='0'+str(rg)
                a=int(el[6]+el[7])
                
                if a>20:
                    l.append(str(rg)+'/'+str(rm)+'/'+'19'+str(a))
                else:
                    l.append(str(rg)+'/'+str(rm)+'/'+'20'+str(a))
        else:
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
