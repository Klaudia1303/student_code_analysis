def Ex5(file):
    import re
    d={}
    k1=0
    k2=0
    k3=0
    k4=0
    k5=0
    f=open(file,encoding="UTF-8")
    pattern_auto=r'[A-Z][A-Z]\d\d\d[A-Z][A-Z]'
    pattern_moto=r'[A-Z][A-Z]\d\d\d\d\d'
    for row in f:
        row=row.strip()
        if len(row)==7:
            auto=re.search(pattern_auto,row)
            moto=re.search(pattern_moto,row)
            if auto:
                k1+=1
                d['auto']=k1
            elif moto:
                k2+=1
                d['moto']=k2
            else:
                k5+=1
                d['errata']=k5
        elif len(row)==5:
            k3+=1
            d['ciclomotore1']=k3
        elif len(row)==6:
            k4+=1
            d['ciclomotore2']=k4
        else:
            k5+=1
            d['errata']=k5
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
