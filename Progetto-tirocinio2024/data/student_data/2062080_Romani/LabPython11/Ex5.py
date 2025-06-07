def Ex5(file):

    import re

    d = {}

    with open(file, encoding = 'UTF-8') as f:

        l = f.readlines()
        s = ''.join(l)

        pattern_auto = r'\b[A-Z][A-Z]\d\d\d[A-Z][A-Z]\b'
        pattern_moto = r'\b[A-Z][A-Z]\d\d\d\d\d\b'
        pattern_ciclomotore1 = r'\b\w\w\w\w\w\b'
        pattern_ciclomotore2 = r'\b\w\w\w\w\w\w\b'

        auto = re.findall(pattern_auto, s)
        moto = re.findall(pattern_moto, s)
        ciclomotore1 = re.findall(pattern_ciclomotore1, s)
        ciclomotore2 = re.findall(pattern_ciclomotore2, s)

        d['auto'] = len(auto)
        d['moto'] = len(moto)
        d['ciclomotore1'] = len(ciclomotore1)
        d['ciclomotore2'] = len(ciclomotore2)

        errata = len(l) - (len(auto)+len(moto)+len(ciclomotore1)+len(ciclomotore2))
        d['errata'] = errata

        
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
