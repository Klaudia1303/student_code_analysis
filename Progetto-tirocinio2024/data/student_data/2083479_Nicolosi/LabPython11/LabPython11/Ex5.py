def Ex5(file):
    fin=open(file,encoding='UTF-8')
    d={'auto':0,'moto':0,'ciclomotore1':0,'ciclomotore2':0,'errata':0}
    formato_auto='[A-Z]{2}[0-9]{3}[A-Z]{2}'
    formato_moto='[A-Z]{2}[0-9]{5}'
    formato_ciclomotore1='[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9[A-Z0-9]'
    formato_ciclomotore2='[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]'
    for riga in fin:
        riga=riga.strip()
        m=re.search(formato_auto,riga)
        if m:
            d['auto']+=1
            continue
        m=re.search(formato_moto,riga)
        if m:
            d['moto']+=1
            continue
        m=re.search(formato_ciclomotore1,riga)
        if m and len(riga)==5:
            d['ciclomotore1']+=1
            continue
        m=re.search(formato_ciclomotore2,riga)
        if m and len(riga)==6:
            d['ciclomotore2']+=1
            continue
        d['errata']+=1
    return d
    
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
