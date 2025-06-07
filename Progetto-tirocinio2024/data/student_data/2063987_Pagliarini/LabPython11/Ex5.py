def Ex5(file):
    f=open(file,encoding='UTF-8')
    patta=r'[A-Z]{2}\d{3}[A-Z]{2}'
    pattm=r'[A-Z]{2}\d{5}'
    pattc1=r'[A-Z0-9]{5}'
    pattc2=r'[A-Z0-9]{6}'
    diz={}
    for i in f:
        i="".join(i.strip().split('\n'))
        print (i)
        if re.match(patta,i) and len(i)==7:
            diz['auto']=diz.get('auto',0)+1
        elif re.match(pattm,i) and len(i)==7:
            diz['moto']=diz.get('moto',0)+1
        elif re.match(pattc1,i) and len(i)==5:
            diz['ciclomotore1']=diz.get('ciclomotore1',0)+1
        elif re.match(pattc2,i)and len(i)==6:
            diz['ciclomotore2']=diz.get('ciclomotore2',0)+1
        else:
            diz['errata']=diz.get('errata',0)+1
    f.close()
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
