def Ex5(file):
    lt=open(file,encoding='UTF-8').read().split('\n')   #lista targhe
    l=['auto','moto','ciclomotore1','ciclomotore2','errata']
    lp=[(r'\b[A-Z]{2}[0-9]{3}[A-Z]{2}\b','auto'),(r'\b[A-Z]{2}[0-9]{5}\b','moto'),\
            (r'\b[A-Z0-9]{5}\b','ciclomotore1'),(r'\b[A-Z0-9]{6}\b','ciclomotore2')]   #lista pattern e chiavi p_c
    d={}
    for el in l:
        d[el]=0
    for targha in lt:
        errata=True
        print(targha)
        for p_c in lp:
            if re.search(p_c[0],targha):
                d[p_c[1]]+=1
                errata=False
                print(p_c[1])
                print(d[p_c[1]])
                break
        if errata:
            d['errata']+=1
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
