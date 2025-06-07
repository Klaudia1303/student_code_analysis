def Ex5(file):
    import re
    veicoli={item:0 for item in ['auto','moto','ciclomotore1','ciclomotore2','errata']}
    with open(file,encoding="UTF-8") as fin:
        Data=[line.strip() for line in fin.readlines()]
    for line in Data:
        if len(line)==7 and re.search(r'[A-Z]{2}\d{3}[A-Z]{2}',line): veicoli['auto']+=1
        elif len(line)==7 and re.search(r'[A-Z]{2}\d{4}',line): veicoli['moto']+=1
        elif len(line)==5 and re.search(r'[A-Z0-9]{5}',line): veicoli['ciclomotore1']+=1
        elif len(line)==6 and re.search(r'[A-Z0-9]{6}',line): veicoli['ciclomotore2']+=1
        else:   veicoli['errata']+=1
    return veicoli
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
