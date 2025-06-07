def Ex5(file):
    d={}
    c=open(file, encoding= 'UTF-8')
    d['auto']=0
    d['moto']=0
    d['ciclomotore1']=0
    d['ciclomotore2']=0
    d['errata']=0
    p=(r'[A-Z]{2,6}[0-9]{0,5}[A-Z]{0,2}')
    pa=('[A-Z]{2}[0-9]{3}[A-Z]{2}')
    pm=('[A-Z]{2}[0-9]{5}')
    pc1=('[A-Z]{0,5}[0-9]{0,5}')
    pc2=('[A-Z]{0,6}[0-9]{0,6}')
    for i in c:            
        m=re.finditer(p,i)
        if not m:
            d['errata']+=1
        else:
            if re.search(pa,i) :
                d['auto']+=1
            elif re.search(pm,i):
                d['moto']+=1
            elif re.search(pc1,i) and len(i)==5:
                d['ciclomotore1']+=1
            elif re.search(pc2,i) and len(i)==6:
                d['ciclomotore2']+=1
            else:
                d['errata']+=1
    c.close()        
    return d
                
            
                
                
            
        


            
                
        
            
            
                
                
            
        
    
    
     


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
