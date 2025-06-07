def Ex5(file):
    import re
    risultato={'auto':0,'moto':0,'ciclomotore1':0,'ciclomotore2':0,'errata':0}
    patternA=r'[A-Z]{2}[0-9]{3}[A-Z]{2}'
    patternM=r'[A-Z]{2}[0-9]{5}'
    patternC1=r'[A-Z0-9]{5}'
    patternC2=r'[A-Z0-9]{6}'
    fin=open(file,encoding='UTF-8')
    for riga in fin:
        riga=riga.strip()
        if re.search(patternA,riga) and len(riga)==7:
            risultato['auto']+=1
        elif re.search(patternM,riga) and len(riga)==7:
            risultato['moto']+=1
        elif re.search(patternC1,riga) and len(riga)==5:
            risultato['ciclomotore1']+=1
        elif re.search(patternC2,riga) and len(riga)==6:
            risultato['ciclomotore2']+=1
        else:
            risultato['errata']+=1
    fin.close()
    return risultato
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
      
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex5, ["targhe1.txt"] , {'auto': 2, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 1})
    counter_test_positivi += tester_fun(Ex5, ["targhe2.txt"] , {'auto': 2, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 2})
    counter_test_positivi += tester_fun(Ex5, ["targhe3.txt"] , {'auto': 3, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 3})
    counter_test_positivi += tester_fun(Ex5, ["targhe4.txt"] , {'auto': 3, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 4})
    counter_test_positivi += tester_fun(Ex5, ["targhe5.txt"] , {'auto': 2, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 5})
    
    print('La funzione',Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
