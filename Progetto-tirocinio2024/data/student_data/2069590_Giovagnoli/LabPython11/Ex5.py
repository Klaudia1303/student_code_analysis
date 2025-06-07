def Ex5(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
    with open(file,encoding="UTF-8") as f:
        lettura=f.read()
        d={}
        pattern={}
        pattern['auto']=r'^([A-Z]{2})(\d{3})([A-Z]{2})$'
        pattern['moto']=r'^([A-Z]{2})(\d{5})$'
        pattern['ciclomotore1']=r'^([A-Z0-9]{5})$'
        pattern['ciclomotore2']=r'^([A-Z0-9]{6})$'
        
        chiavi=['auto','moto', 'ciclomotore1', 'ciclomotore2']
        
        for i in chiavi:
            ricerca=re.findall(pattern[i],lettura,re.MULTILINE)
            
            c=len(ricerca)
            d[i]=c

    indice=0
    with open(file,encoding="UTF-8") as f1:
        for rriga in f1:
            indice+=1
    somma=sum(d.values())
    d['errata']=(indice-somma)
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
