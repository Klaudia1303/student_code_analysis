def Ex5(file):
    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    d={}
    tipologia=['auto','moto','ciclomotore1','ciclomotore2','errata']
    for i in tipologia:
        d[i]=0
    #HO IL DIZIONARIO
    f=open(file,encoding='UTF-8')
    pattern_auto= r'\b([A-Z])([A-Z])([0-9])([0-9])([0-9])([A-Z])([A-Z])\b'
    pattern_moto= r'\b([A-Z])([A-Z])([0-9])([0-9])([0-9])([0-9])([0-9])\b'
    pattern_c1= r'\b([A-Z0-9])([A-Z0-9])([A-Z0-9])([A-Z0-9])([A-Z0-9])\b'
    pattern_c2= r'\b([A-Z0-9])([A-Z0-9])([A-Z0-9])([A-Z0-9])([A-Z0-9])([A-Z0-9])\b'
    import re
    for i in f:
        a=re.search(pattern_auto,i)
        m=re.search(pattern_moto,i)
        c1=re.search(pattern_c1,i)
        c2=re.search(pattern_c2,i)
        if a:
            d['auto']+=1
        elif m:
            d['moto']+=1
        elif c1:
            d['ciclomotore1']+=1
        elif c2:
            d['ciclomotore2']+=1
        else:
            d['errata']+=1
    return d
      
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
