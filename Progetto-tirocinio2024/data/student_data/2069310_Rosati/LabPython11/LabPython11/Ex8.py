def Ex8(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(file,'r',encoding='UTF-8').readlines()
    lista=[]
    pattern=r'\b[A-Z]{3} ?[A-Z]{3} ?(\d\d)([A-Z])(\d\d) ?[A-Z]\d\d\d[A-Z]\b'
    diz={'A':'01','B':'02','C':'03','D':'04','E':'05','H':'06','L':'07','M':'08','P':'09','R':'10','S':'11','T':'12'}
    num_giorni_mese = {'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
    giorno=0
    mese=''
    anno=''
    data=''
    for riga in f:
           giorno=0
           mese=''
           anno=''
           data=''
           num=re.search(pattern,riga)
           if re.match(pattern,riga):
               if num.group(2) not in diz:
                  lista.append("Mese errato")
               else:
                  mese=diz[num.group(2)]
                  if 32<=int(num.group(3))<=40:
                     lista.append("Giorno errato")
                  else:
                      if int(num.group(3))>=41:
                         if 1<=int(num.group(3))-40<=31:
                            giorno=int(num.group(3))-40
                         else:
                            lista.append("Giorno errato") 
                      elif 1<=int(num.group(3))<=31:
                           giorno=int(num.group(3))
                      if int(num.group(1))<=20:
                         anno='20'+num.group(1)
                      else:
                         anno='19'+num.group(1)
                      if giorno!=0:
                         if giorno < 10:
                            giorno="0"+str(giorno)
                         if int(giorno)<=num_giorni_mese[mese]:
                            data=str(giorno)+"/"+mese+"/"+anno
                            lista.append(data)
                         else:
                            lista.append("Giorno errato")
           else:
               lista.append("Codice errato")
    return lista



    
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex8, ["codici1.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici2.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici3.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921'])
    counter_test_positivi += tester_fun(Ex8, ["codici4.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931'])
    counter_test_positivi += tester_fun(Ex8, ["codici5.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931', 'Codice errato', 'Giorno errato'])

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
