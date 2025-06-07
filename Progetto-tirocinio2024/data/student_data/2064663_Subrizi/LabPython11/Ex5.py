def Ex5(file):
       fopen=open(file,'r',encoding='UTF-8')
       d={}
       d['auto']=0
       d['moto']=0
       d['ciclomotore1']=0
       d['ciclomotore2']=0
       d['errata']=0
       auto=r'^[A-Z]{2}[0-9]{3}[A-Z]{2}$'
       moto=r'^[A-Z]{2}[0-9]{5}$'
       ciclomotore1=r'^[A-Z0-9]{5}$'
       ciclomotore2=r'^[A-Z0-9]{6}$'
       for riga in fopen:
              riga=riga.strip()
              if len(re.findall(auto,riga))>=1:
                     d['auto']=int(d['auto'])+1
                     continue
              elif len(re.findall(moto,riga))>=1:
                     d['moto']=int(d['moto'])+1
                     continue
              elif len(re.findall(ciclomotore1,riga))>=1:
                     d['ciclomotore1']=int(d['ciclomotore1'])+1
                     continue
              elif len(re.findall(ciclomotore2,riga))>=1:
                     d['ciclomotore2']=int(d['ciclomotore2'])+1
                     continue
              else:
                     d['errata']=int(d['errata'])+1
       fopen.close()              
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
