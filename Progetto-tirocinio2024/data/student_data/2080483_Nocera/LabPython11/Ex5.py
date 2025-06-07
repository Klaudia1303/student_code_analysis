def Ex5(file):
    fin=open(file,encoding="UTF-8")
    testo=fin.read()
    patternauto=r"\b[A-Z]{2}[0-9]{3}[A-Z]{2}\b"
    patternmoto=r"\b[A-Z]{2}[0-9]{5}\b"
    patternciclomotore1=r"\b[A-Z0-9]{5}\b"
    patternciclomotore2=r"\b[A-Z0-9]{6}\b"
    patternerrore=r"\b[A-Za-z0-9]+\b"
    riserrore=re.findall(patternerrore,testo)
    risauto=re.findall(patternauto,testo)
    rismoto=re.findall(patternmoto,testo)
    risciclomotore1=re.findall(patternciclomotore1,testo)
    risciclomotore2=re.findall(patternciclomotore2,testo)
    for elem in riserrore.copy():
        if elem in risauto:
            riserrore.remove(elem)
        elif elem in rismoto:
            riserrore.remove(elem)
        elif elem in risciclomotore1:
            riserrore.remove (elem)
        elif elem in risciclomotore2:
            riserrore.remove(elem)
    print(riserrore)
    diz={"auto":len(risauto),"moto":len(rismoto),"ciclomotore1":len(risciclomotore1),"ciclomotore2":len(risciclomotore2),"errata":len(riserrore)}
    return diz
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
