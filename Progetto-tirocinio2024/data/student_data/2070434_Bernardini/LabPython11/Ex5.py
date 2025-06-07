def Ex5(file):
    d={}
    d['auto']=0
    d['moto']=0
    d['ciclomotore1']=0
    d['ciclomotore2']=0
    d['errata']=0
    a=open(file,'r',encoding='UTF-8')
    for f in a:
        riga=''.join(f.strip().split('\n'))
        pattern1=r'[A-Z]{2}\d{3}[A-Z]{2}'
        pattern2=r'[A-Z]{2}\d{5}'
        pattern3=r'[A-Z0-9]{5}'
        pattern4=r'[A-Z0-9]{6}'
        if re.match(pattern1,riga) and len(riga)==7:
            d['auto']+=1
        elif re.match(pattern2,riga) and len(riga)==7:
            d['moto']+=1
        elif re.match(pattern3,riga) and len(riga)==5:
            d['ciclomotore1']+=1
        elif re.match(pattern4,riga) and len(riga)==6:
            d['ciclomotore2']+=1
        else:
            d['errata']+=1
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
