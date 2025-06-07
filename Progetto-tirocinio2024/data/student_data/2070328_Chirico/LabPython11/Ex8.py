def Ex8(file):
    x = open(file,'r',encoding = 'UTF-8')
    l = []

    pattern = r'\b[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})((([A,C,E,L,M,R,T])(([0-3][0-9])|([4-6][1-9])|(7[0-1])))|(([D,H,P,S])(([0-3][0-9])|([4-6][1-9])|70))|(([B])|(([0-3][0-9])|([4-5][0-9])|6[0-8]))) ?[A-Z][0-9]{3}[A-Z]\b' #sintassi codice giusto

    pattern_correttezza = r'\b[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})[A-Z][0-9]{2} ?[A-Z][0-9]{3}[A-Z]\b'

    pattern_mesi = r'^\b([A-Z]|[0-9]){3} ?([A-Z]|[0-9]){3} ?([0-9]{2})[A,B,C,D,E,H,L,M,P,R,S,T]'

    
    for i in x:
        a = re.search(pattern, i)
        if a:
            #ANNO
            if int(a.group(1)) <= 20:
                aa ='20'+a.group(1)
            else:
                aa ='19'+a.group(1)


            
            #GIORNO
            if a.group(4):
                mm = a.group(4)
                if int(a.group(5)) > 40:
                    gg = int(a.group(5))-40
                else:
                    gg = int(a.group(5))
      
            elif a.group(10):
                mm = a.group(10)
                if int(a.group(11)) > 40:
                    gg = int(a.group(11))-40
                else:
                    gg = int(a.group(11))
        
            elif a.group(15):
                mm = a.group(15)
                if int(a.group(16)) > 40:
                    gg = int(a.group(16))-40
                else:
                    gg = int(a.group(16))

            if len(str(gg)) == 1:
                gg = '0'+str(gg)
            else:
                gg = str(gg)



            #MESE
            if mm == 'A':
                mm = '01'
            elif mm == 'B':
                mm = '02'
            elif mm == 'C':
                mm = '03'
            elif mm == 'D':
                mm = '04'
            elif mm == 'E':
                mm = '05'
            elif mm == 'H':
                mm = '06'
            elif mm == 'L':
                mm = '07'
            elif mm == 'M':
                mm = '08'
            elif mm == 'P':
                mm = '09'
            elif mm == 'R':
                mm = '10'
            elif mm == 'S':
                mm = '11'
            elif mm == 'T':
                mm = '12'
            

            l.append(gg+'/'+mm+'/'+aa)

        else:
            b = re.search(pattern_correttezza, i)
            c = re.search(pattern_mesi, i, flags = re.MULTILINE)
            if not b:
                l.append('Codice errato')
            elif not c:
                l.append('Mese errato')
            else:
                l.append('Giorno errato')

    x.close()     
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
