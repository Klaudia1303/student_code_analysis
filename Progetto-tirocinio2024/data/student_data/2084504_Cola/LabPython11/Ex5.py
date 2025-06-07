def Ex5(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
    f=open(file,encoding='UTF-8')
    s=f.read()
    f.close()
    d={}
    print(s)
    d['auto']=len(re.findall(r'[A-Z]{2}[0-9]{3}[A-Z]{2}$',s,re.MULTILINE))
    d['moto']=len(re.findall(r'^[A-Z]{2}[0-9]{5}$',s,re.MULTILINE))
    d['ciclomotore1']=len(re.findall(r'^[A-Z0-9]{5}$',s,re.MULTILINE))
    d['ciclomotore2']=len(re.findall(r'^[A-Z0-9]{6}$',s,re.MULTILINE))
    d['errata']=len(s.strip().split())-d['auto']-d['moto']-d['ciclomotore1']-d['ciclomotore2']
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
