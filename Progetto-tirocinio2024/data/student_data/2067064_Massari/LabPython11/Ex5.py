def Ex5(file):
    f=open(file,encoding="UTF-8")
    fr=f.readlines()
    l=[]
    import re
    for elem in fr:
        l.append(elem.strip().split())
    lp=[(r'\b[A-Z]{2}[0-9]{3}[A-Z]{2}\b','auto'), (r'\b[A-Z]{2}[0-9]{5}\b','moto'), (r'\b[A-Z0-9]{5}\b','ciclomotore1') , (r'\b[A-Z0-9]{6}\b','ciclomotore2')]
    diz_res={}
    contatore=0
    for y in range(len(l)):
        targa=l[y][0]
        contatore=0
        for x in range(len(lp)):
            pattern=lp[x][0]
            veicolo=lp[x][1]
            i=re.search(pattern,targa)
            if i:
                if veicolo not in diz_res:
                    diz_res[veicolo]=1
                else:
                    diz_res[veicolo]+=1
                contatore+=1

        if contatore==0:
            if 'errata' not in diz_res:
                diz_res['errata']=1
            else:
                diz_res['errata']+=1
                
    
                
    f.close()       
    
    return diz_res
       
            
            
    

    
    
            
    
    


    
        
   






















    
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
