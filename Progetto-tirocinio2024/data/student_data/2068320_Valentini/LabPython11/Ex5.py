def Ex5(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
    l = open(file)
    r = l.readlines()
    contaauto=0
    contamoto=0
    contaciclomotore1=0
    contaciclomotore2=0
    contaerrore = 0
    pattern = [r'\b[A-Z][A-Z]\d\d\d[A-Z][A-Z]\b',r'\b[A-Z][A-Z]\d\d\d\d\d\b',r'\b\w\w\w\w\w\b',r'\b\w\w\w\w\w\w\b']
    for i in range(len(r)):
        targa = str(r[i].strip())
        for k in range(0,4):
            num = re.match(pattern[k], targa)
            if num:
                if k == 0:
                    contaauto +=1
                    break
                elif k == 1:
                    contamoto +=1
                    break
                elif k == 2:
                    contaciclomotore1 += 1
                    break
                elif k == 3:
                    contaciclomotore2 += 1
                    break                
            else:
                continue
        if not num:
            contaerrore += 1
    dizionario = {}
    dizionario['auto'] = int(contaauto)
    dizionario['moto'] = int(contamoto)
    dizionario['ciclomotore1'] = int(contaciclomotore1)
    dizionario['ciclomotore2'] = int(contaciclomotore2)
    dizionario['errata'] = int(contaerrore)
    return(dizionario)
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
