def Ex5(file):
    import re
    a=open(file, 'r',encoding='UTF-8').read()
    a=len(re.findall('[A-Z][A-Z]\d\d\d[A-Z][A-Z]',a,re.IGNORECASE))
    m=len(re.findall('[A-Z][A-Z]\d\d\d\d\d',a,re.IGNORECASE))
    c1=len(re.findall('\b\b\b\b\b',a,re.IGNORECASE))
    c2=len(re.findall('\b\b\b\b\b\b',a,re.IGNORECASE))
    e=len(open(file).read().split('\n'))-a-m-c1-c2
    d={'auto':a,'moto':m,'ciclomotore1':c1,'ciclomotore2':c2,'errata':e}
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
