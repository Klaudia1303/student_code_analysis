def Ex5(file):
    import re
    fin=open(file,"r",encoding="UTF-8")
    d={}
    d['auto']=0
    d['moto']=0
    d['ciclomotore1']=0
    d['ciclomotore2']=0
    d['errata']=0
    pattern1='[A-Z]{2}[0-9]{3}[A-Z]{2}'
    pattern2='[A-Z]{2}[0-9]{5}'
    pattern3='[A-Z0-9]{5}'
    pattern4='[A-Z0-9]{6}'
    for riga in fin:
        riga=riga.strip()
        m=re.search(pattern1, riga)
        if m:
            d['auto']+=1
            continue
        m=re.search(pattern2, riga)
        if m:
            d['moto']+=1
            continue
        m=re.search(pattern3, riga)
        if m and len(riga)==5:
            d['ciclomotore1']+=1
            continue
        m=re.search(pattern4, riga)
        if m and len(riga)==6:
            d['ciclomotore2']+=1
            continue
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
