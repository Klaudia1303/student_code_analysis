def Ex8(file):
   f = open(file, encoding='UTF-8')
   s = f.readlines()
   f.close()
   pattern = r'[A-Z]{3} ?[A-Z]{3} ?\d\d[A-Z]\d\d ?[A-Z]\d\d\d[A-Z]'
   l = []
   d = {'A':['01',31],'B':['02',28],'C':['03',31],'D':['04',30],'E':['05',31],'H':['06',30],'L':['07',31],'M':['08',31],'P':['09',30],'R':['10',31],'S':['11',30],'T':['12',31]}
   for riga in s:
       if re.match(pattern, riga):
           riga = riga.replace(' ','')
           p1 = riga[:6]
           anno = riga[6:8]
           mese = riga[8]
           giorno = riga[9:11]
           fine = riga[11:]
           if mese not in 'ABCDEHLMPRST':
               l.append('Mese errato')
           else:
               num_mese=d[mese][0]
               giorni_mese=d[mese][1]
               if 1<=int(giorno)<=giorni_mese:
                   if 1<=int(giorno)<=9:
                       ris='0'+str(giorno)+'/'+d[mese][0]+'/'
                   else:
                       ris=str(giorno)+'/'+d[mese][0]+'/'
                   if 0<=int(anno)<=20:
                       ris=ris+'20'+anno
                   elif 20<=int(anno)<=99:
                       ris=ris+'19'+anno
                   l.append(ris)
                   ris=str()
               elif 1<=int(giorno)-40<=giorni_mese:
                   if 1<=int(giorno)-40<=9:
                       ris='0'+str(int(giorno)-40)+'/'+d[mese][0]+'/'
                   else:
                       ris=str(int(giorno)-40)+'/'+d[mese][0]+'/'
                   if 0<=int(anno)<=20:
                       ris=ris+'20'+anno
                   elif 20<int(anno)<=99:
                       ris=ris+'19'+anno
                   l.append(ris)
                   ris=str()
               else:
                   l.append('Giorno errato')
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
