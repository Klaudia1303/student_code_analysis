def Ex8(file):
    fopen=open(file,'r',encoding='UTF-8')
    fread=fopen.readlines()
    pattern=r'[A-Z]{3}\W*[A-Z]{3}\W*(\d\d)([A-Z])(\d\d)\W*[A-Z][0-9]{3}[A-Z]'
    d={}
    d={'A':'01','B':'02','C':'03','D':'04','E':'05','H':'06','L':'07','M':'08','P':'09','R':'10','S':'11','T':'12'}
    mesi30='DHPS'
    mesi31='ACELMRT'
    mesespec='B'
    mesi=mesi30+mesi31+mesespec
    lr=[]
    for riga in fread:
        riga=riga.strip()
        m=re.search(pattern,riga)
        if m:
            anno=m.group(1)
            mese=m.group(2)
            giorno=m.group(3)
            if int(anno)<=20:
                anno='20'+anno
            elif int(anno)>20:
                anno='19'+anno
            if int(giorno)>39:
                if int(giorno)-40<10:
                    giorno='0'+str(int(giorno)-40)
                else:
                    giorno=str(int(giorno)-40)
            if mese not in mesi:
                lr.append('Mese errato')
            elif mese in mesi30 and int(giorno)<1 or int(giorno)>30:
                lr.append('Giorno errato')
            elif mese in mesi31 and int(giorno)<1 or int(giorno)>31:
                lr.append('Giorno errato')
            elif mese in mesespec and int(giorno)<1 or int(giorno)>28:
                lr.append('Giorno errato')
            else:
                lr.append(giorno+'/'+d[mese]+'/'+anno)
        else:
            lr.append('Codice errato')
    fopen.close()
    return lr



            
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
