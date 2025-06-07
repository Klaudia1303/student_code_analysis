def Ex8(file):
    f=open(file, 'r', encoding='UTF-8')
    u=f.readlines()
    mesi='ABCDEHLMPRST'
    import re
    l=[]
    mese=''
    pattern=r'\b[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})([A-Z])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]\b'
    for riga in u:
        r=riga.strip()
        a=re.findall(pattern, r)
        if a==[]:
            l.append('Codice errato')
            continue
        else:
            for j in range(len(a)):
                s=a[j]
                gg=s[2]
                me=s[1]
                an=s[0]
        if int(an)>20:
            anno='19'+str(an)
        else:
            anno='20'+str(an)
        if me=='B':
            mese='02'
            if (int(gg)<=28):
                giorno=str(gg)
                if len(giorno)==1:
                    giorno='0'+giorno
                datacompleta=giorno+'/'+mese+'/'+anno
                l.append(datacompleta)
            elif (int(gg)>40) and int(gg)<=68:
                gg=int(gg)-40
                giorno=str(gg)
                if len(giorno)==1:
                    giorno='0'+giorno
                datacompleta=giorno+'/'+mese+'/'+anno
                l.append(datacompleta)
            else:
                l.append('Giorno errato')
        elif me in 'ACELMRT':
            for i in range(len(mesi)):
                if me==mesi[i]:
                    me=i+1
                    if me<10:
                        mese='0'+str(me)
                    else:
                        mese=str(me)
            if (int(gg)<=30):
                giorno=str(gg)
                if len(giorno)==1:
                    giorno='0'+giorno
                datacompleta=giorno+'/'+mese+'/'+anno
                l.append(datacompleta)
            elif (int(gg)>40) and int(gg)<=70:
                gg=int(gg)-40
                giorno=str(gg)
                if len(giorno)==1:
                    giorno='0'+giorno
                datacompleta=giorno+'/'+mese+'/'+anno
                l.append(datacompleta)
            else:
                l.append('Giorno errato')
        elif me in 'DHPS':
            for i in range(len(mesi)):
                if me==mesi[i]:
                    me=i+1
                    if me<10:
                        mese='0'+str(me)
                    else:
                        mese=str(me)
            if (int(gg)<=31):
                giorno=str(gg)
                if len(giorno)==1:
                    giorno='0'+giorno
                datacompleta=giorno+'/'+mese+'/'+anno
                l.append(datacompleta)
            elif (int(gg)>40) and int(gg)<=71:
                gg=int(gg)-40
                giorno=str(gg)
                if len(giorno)==1:
                    giorno='0'+giorno
                datacompleta=giorno+'/'+mese+'/'+anno
                l.append(datacompleta)
            else:
                l.append('Giorno errato')
        elif me not in mesi:
            l.append('Mese errato')
    f.close()
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
