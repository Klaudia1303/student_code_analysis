def Ex5(file):
    f = open(file,encoding="UTF-8")
    auto = r'[A-Z]{2}\d{3}[A-Z]{2}'
    moto = r'[A-Z]{2}\d{5}'
    ciclo1 = r'[A-Z0-9]{5}'
    ciclo2 = r'[A-Z0-9]{6}'
    d = {'auto':0,'moto':0,'ciclomotore1':0,'ciclomotore2':0,'errata':0}
    for i in f:
        s = "".join(i.strip().split("\n"))
        if re.match(auto,s) and len(s)==7:
            d['auto'] = d['auto'] + 1
        elif re.match(moto,s) and len(s)==7:
            d['moto'] = d['moto'] + 1
        elif re.match(ciclo1,s) and len(s)==5:
            d['ciclomotore1'] = d['ciclomotore1'] + 1
        elif re.match(ciclo2,s) and len(s)==6:
            d['ciclomotore2'] = d['ciclomotore2'] + 1
        else:
            d['errata'] = d['errata'] + 1
    f.close()
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
