def Ex8(file):
    L=[]
    Mesi={'A':'01','B':'02','C':'03','D':'04','E':'05','H':'06','L':'07','M':'08','P':'09','R':'10','S':'11','T':'12',}
    fin=open(file)
    s=fin.read()
    data=''
    i=0
    generale=r'[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]'
    while i<len(s):
        if s[i]==' ':
            s=s[0:i]+s[i+1:len(s)]
        else:
            i=i+1
    #print(s)
    s=s.split()
    #print(s)
    for codice in s:
        data=''
        if re.search(generale,codice,flags=re.MULTILINE)==None or len(codice)!=16:
            #print(codice)
            L.append('Codice errato')
        else:
            nascita=codice[6:11]
            #print(nascita)
            if 31<int(nascita[3:5])<41 or int(nascita[3:5])>71:
                L.append('Giorno errato')
                continue
            if (nascita[2]=='B'and 28<int(nascita[3:5])<31)or(nascita[2]in['S','D','H','P'] and int(nascita[3:5])==31):
                L.append('Giorno errato')
                continue
            if nascita[2] not in Mesi:
                L.append('Mese errato')
                continue
            if int(nascita[3:5])>=41:
                if int(nascita[3:5])-40<10: 
                     data='0'+str(int(nascita[3:5])-40)
                else:
                    data=str(int(nascita[3:5])-40)

            else:
                data=nascita[3:5]
            data=data+'/'+Mesi[nascita[2]]+'/'    
            if int(nascita[0:2])>20:
                data=data+'19'+nascita[0:2]
            else:
                data=data+'20'+nascita[0:2]
            #print(data)    

            L.append(data)    
    return L
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
