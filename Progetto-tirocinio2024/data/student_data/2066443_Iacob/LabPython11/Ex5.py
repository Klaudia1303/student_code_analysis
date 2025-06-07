def Ex5(file):
    o = open(file,encoding="UTF-8")
    p_auto = r'[A-Z]{2}\d{3}[A-Z]{2}'
    p_moto = r'[A-Z]{2}\d{5}'
    p_ciclo1 = r'[A-Z0-9]{5}'
    p_ciclo2 = r'[A-Z0-9]{6}'
    diz = {'auto':0,'moto':0,'ciclomotore1':0,'ciclomotore2':0,'errata':0}
    for i in o:
        x = "".join(i.strip().split("\n"))
        if re.match(p_auto,x) and len(x)==7:
            diz['auto'] += 1
        elif re.match(p_moto,x) and len(x)==7:
            diz['moto'] += 1
        elif re.match(p_ciclo1,x) and len(x)==5:
            diz['ciclomotore1'] += 1
        elif re.match(p_ciclo2,x) and len(x)==6:
            diz['ciclomotore2'] += 1
        else:
            diz['errata'] += 1
    o.close()
    return diz
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
