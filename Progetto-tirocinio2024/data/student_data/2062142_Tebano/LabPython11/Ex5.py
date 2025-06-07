def Ex5(file):
    fin=open(file)
    s=fin.read()
    d={'auto':0,'moto':0,'ciclomotore1':0,'ciclomotore2':0,'errata':0}
    auto=r'([A-Z]{2}[0-9]{3}[A-Z]{2})'
    moto=r'([A-Z]{2}[0-9]{5})'
    ciclomotore1=r'([A-Z]{5}|[0-9]{5})'
    ciclomotore2=r'([A-Z]{5}|[0-9]{5})'
    d['auto']=len(re.findall(auto,s))
    print(re.findall(auto,s))
    d['moto']=len(re.findall(moto,s))
    print(re.findall(moto,s))
    d['ciclomotore1']=len(re.findall(ciclomotore1,s))
    d['ciclomotore2']=len(re.findall(ciclomotore2,s))
    d['errata']=len(re.findall(r'\b\w+\b',s))-d['auto']-d['moto']-d['ciclomotore1']-d['ciclomotore2']
    print(re.findall(r'\b\w*\b',s))
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
