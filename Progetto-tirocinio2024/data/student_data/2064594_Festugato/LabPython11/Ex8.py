def Ex8(file):
    import re
    risultato = list()
    f = open(file,'r',encoding='UTF-8')

    codice_fiscale = r'\b([A-Z]{3}) ?([A-Z]{3}) ?([\d]{2})([A-Z])([\d]{2}) ?([A-Z][\d]{3}[A-Z])\b'

   
    mesi = ['A','B','C','D','E','H','L','M','P','R','S','T']
    mesi = {'A':('01','31'),'B':('02','28'), 'C':('03','31'), 'D':('04','30'), 'E':('05','31'),'H':('06','30'),'L':('07','31'),'M':('08','31'),'P':('09','30'),
            'R':('10','31'),'S':('11','30'),'T':('12','31')}
    

    for codice in f:
        
        m = re.search(codice_fiscale,codice)

        if m == None:
            print('Codice errato',codice)
            risultato.append('Codice errato')
            continue
        else:
            codice = m.group()
            nome = m.group(1)
            cognome = m.group(2)
            anno = m.group(3)
            mese= m.group(4)
            giorno = m.group(5)
            comune = m.group(6)

            if mese not in mesi:
                risultato.append('Mese errato')
                print('Mese errato',codice,mese)
                continue
            elif int(giorno) >= 71 or 31<int(giorno)<=40 or ( int(giorno) <= 31 and int(giorno) > int(mesi[mese][1])): #31 + 40
                print(int(giorno), int(mesi[mese][1]))
                risultato.append('Giorno errato')
                print('Giorno errato',codice,giorno)
                continue
            else:
                if int(giorno) <= 31 and int(giorno) < int(mesi[mese][1]):

                     if int(giorno) <= 10:

                        if int(anno) <= 20:
                    
                            nascita= '0'+giorno+'/'+mesi[mese][0]+'/20'+anno
                            print(nascita,codice)
                            risultato.append(nascita)
                        else:
                            nascita= '0'+giorno+'/'+mesi[mese][0]+'/19'+anno
                            print(nascita,codice)
                            risultato.append(nascita)
                     else:
                        if int(anno) <= 20:
                    
                            nascita= giorno+'/'+mesi[mese][0]+'/20'+anno
                            print(nascita,codice)
                            risultato.append(nascita)
                        else:
                            nascita= giorno+'/'+mesi[mese][0]+'/19'+anno
                            print(nascita,codice)
                            risultato.append(nascita)
                        
                        
                elif int(giorno) > 40 and (int(giorno)-40) < int(mesi[mese][1]):

                    if 41<=int(giorno)<=49:
                    
                        if int(anno) <= 20:
                    
                             nascita= '0'+str(int(giorno)-40)+'/'+mesi[mese][0]+'/20'+anno
                             print(nascita,codice)
                             risultato.append(nascita)
                        else:
                            nascita= '0'+str(int(giorno)-40)+'/'+mesi[mese][0]+'/19'+anno
                            print(nascita,codice)
                            risultato.append(nascita)
                
                    else:
                        if int(anno) <= 20:
                    
                             nascita= str(int(giorno)-40)+'/'+mesi[mese][0]+'/20'+anno
                             print(nascita,codice)
                             risultato.append(nascita)
                        else:
                            nascita= str(int(giorno)-40)+'/'+mesi[mese][0]+'/19'+anno
                            print(nascita,codice)
                            risultato.append(nascita)
                        
                    
    #print('fine')

    return risultato
    





    

    
    
    
    




































   
    
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
