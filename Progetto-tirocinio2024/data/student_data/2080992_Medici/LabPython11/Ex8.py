def Ex8(file):
    file=open(file, encoding='UTF-8')
    l=[]
    mesi=['A','B','C','D','E','H','L','M','P','R','S','T']
    lmesi=['01','02','03','04','05','06','07','08','09','10','11','12']
    for riga in file:
        s=''
        anno=''
        mese=''
        giorno=''
        pattern= r'(\s?[A-Z]{3})\s?(\s?[A-Z]{3})\s?(\d\d[A-Z]\d\d)\s?([A-Z]\d\d\d[A-Z])\s?'
        m=re.search(pattern, riga)
        if m:
            controllo=mese
            for i in range(12):
                if m.group(3)[2]==mesi[i]:
                    mese+=lmesi[i]
            if mese==controllo:
                s='Mese errato'
                l.append(s)
                continue
            giorno+=m.group(3)[3]
            giorno+=m.group(3)[4]
            giorno=int(giorno)
            if giorno>40:
                giorno-=40
            if giorno==40:
                s='Giorno errato'
                l.append(s)
                continue
            if mese=='04' or mese=='06' or mese=='09' or mese=='11':
                giorno=int(giorno)
                if giorno>30:
                    s='Giorno errato'
                    continue
            elif mese=='02':
                giorno=int(giorno)
                if giorno>29:
                    s='Giorno errato'
                    continue
            else:
                giorno=int(giorno)
                if giorno>31:
                    s='Giorno errato'
                    continue
            if int(giorno)<10:
                    giorno=str(giorno)
                    giorno='0'+giorno
            giorno=str(giorno)
            s+=giorno
            s+='/'
            s+=mese
            s+='/'
            anno+=m.group(3)[0]
            anno+=m.group(3)[1]
            anno=int(anno)
            if anno<=20:
                s+='20'
                anno=str(anno)
                s+=anno
            else:
                s+='19'
                anno=str(anno)
                s+=anno
        else:
            s='Codice errato'
        l.append(s)
    file.close()
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
