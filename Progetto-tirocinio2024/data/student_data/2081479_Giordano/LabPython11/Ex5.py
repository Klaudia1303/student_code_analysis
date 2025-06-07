def Ex5(file):
    import re
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
    targhe={'auto': 0, 'moto': 0, 'ciclomotore1': 0, 'ciclomotore2': 0, 'errata': 0}     
    with open(file, encoding='UTF-8') as file:

        txt=file.readline()
        txt=txt.strip()
        while txt!='':
            if re.match(r'[A-Z][A-Z]\d\d\d[A-Z][A-Z]',txt):
                print(txt)
                targhe['auto']+=1
            elif re.match(r'[A-Z][A-Z]\d\d\d\d\d',txt):
                targhe['moto']+=1
            elif re.match(r'[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]',txt) and len(txt)==6:
                targhe['ciclomotore2']+=1
            elif re.match(r'[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]',txt) and len(txt)==5:
                targhe['ciclomotore1']+=1
            else:
                targhe['errata']+=1
            txt=file.readline()
            txt=txt.strip()
    print(targhe)
    return targhe



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
