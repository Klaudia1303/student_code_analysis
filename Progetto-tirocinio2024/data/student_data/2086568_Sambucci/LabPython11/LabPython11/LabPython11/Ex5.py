def Ex5(file):
    import re
    fin=open(file,encoding="UTF-8")
    targhe=fin.readlines()
    fin.close()
    diz={'auto': 0,'moto': 0 ,'ciclomotore1': 0 ,'ciclomotore2': 0 ,'errata': 0}
    patternauto=r'[A-Z]{2}[0-9]{3}[A-Z]{2}'
    patternmoto=r'[A-Z]{2}[0-9]{5}'
    patternciclomotore1=r'[A-Z0-9]{5}'
    patternciclomotore2=r'[A-Z0-9]{6}'
    for t in targhe:
        t=t.strip()
        if len(t)==7:
            m=re.search(patternauto,t)
            n=re.search(patternmoto,t)
            if m:
                diz['auto']+=1
            elif n:
                diz['moto']+=1
            elif m==None and n==None:
                diz['errata']+=1
        elif len(t)==5:
            m=re.search(patternciclomotore1,t)
            if m:
                diz['ciclomotore1']+=1
            else:
                diz['errata']+=1
        elif len(t)==6:
            m=re.search(patternciclomotore2,t)
            if m:
                diz['ciclomotore2']+=1
            else:
                diz['errata']+=1
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
