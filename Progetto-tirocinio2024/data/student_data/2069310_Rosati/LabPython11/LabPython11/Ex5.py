def Ex5(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    import re
    f=open(file,'r',encoding='UTF-8').readlines()
    diz={'auto':0,'moto':0,'ciclomotore1':0,'ciclomotore2':0,'errata':0}
    auto=r'\b[A-Z]{2}\d{3}[A-Z]{2}\b'
    moto=r'\b[A-Z]{2}\d{5}\b'
    ciclomotore1=r'\b[A-Z0-9]{5}\b'
    ciclomotore2=r'\b[A-Z0-9]{6}\b'
    for riga in f:
        if re.search(auto,riga):
           diz['auto']+=1
        elif re.search(moto,riga):
             diz['moto']+=1
        elif re.search(ciclomotore1,riga):
             diz['ciclomotore1']+=1
        elif re.search(ciclomotore2,riga):
             diz['ciclomotore2']+=1
        else:
             diz['errata']+=1
    return diz
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
