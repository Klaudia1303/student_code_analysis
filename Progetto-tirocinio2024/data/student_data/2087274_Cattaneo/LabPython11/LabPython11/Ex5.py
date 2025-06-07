def Ex5(file):
    d={}
    f=open(file,'r',encoding='UTF-8')
    auto=['auto',r'[A-Z]{2}[0-9]{3}[A-Z]{2}']
    moto=['moto',r'[A-Z]{2}[0-9]{5}']
    ciclomotore1=['ciclomotore1',r'[0-9A-Z]{5}']
    ciclomotore2=['ciclomotore2',r'[0-9A-Z]{6}']
    patterns=[auto,moto,ciclomotore1,ciclomotore2]
    for categoria in patterns:
        d[categoria[0]]=0
    d['errata']=0
    for line in f:
        line=line.strip()
        flag=True
        for pattern in patterns:
            if re.search(pattern[1],line):
                if line==re.search(pattern[1],line).group():
                    d[pattern[0]]+=1
                    flag=False
        if flag:
            d['errata']+=1
    f.close()
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
