def Ex8(file):
    f=open(file, encoding='UTF-8')
    l=f.readlines()
    f.close()
    res=[]
    d={}
    j=1
    for i in 'ABCDEHLMPRST':
        if(j<10):
            d[i]='0'+str(j)
        else:
            d[i]=str(j)
        j+=1
    for i in range(len(l)):
        s=l[i]
        pattern=r'([A-Z]{3} [A-Z]{3} |[A-Z]{6}|[A-Z]{3} [A-Z]{3}|[A-Z]{6} )(\d{2}[A-Z]\d{2}|\d{2}[A-Z]\d{2} )([A-Z]\d{3}[A-Z])'
        cod=re.search(pattern, s)
        if cod!=None:
            pattern2=r'\d{2}[A-Z]\d{2}'
            data=re.search(pattern2, cod.group())
            giorno=data.group()[3:]
            mese=data.group()[2]
            anno=data.group()[:2]
            if((int(giorno)>=1 and int(giorno)<=31) or (int(giorno)>=40 and int(giorno)<=71) and mese in d):
                if(int(anno)<=20):
                    if(int(giorno)>28 and mese=='B' or int(giorno)>31 and int(giorno)<=40):
                        res.append('Giorno errato')
                    else:
                        if(int(giorno)<=31):
                            res.append(giorno+'/'+d[mese]+'/'+'20'+anno)
                        elif(int(giorno)>40 and int(giorno)<50):
                            res.append('0'+str(int(giorno)-40)+'/'+d[mese]+'/'+'20'+anno)
                        else:
                            res.append(str(int(giorno)-40)+'/'+d[mese]+'/'+'20'+anno)
                            
                else:
                    if(int(giorno)>28 and mese=='B' or int(giorno)>31 and int(giorno)<=40):
                        res.append('Giorno errato')
                    else:
                        if(int(giorno)<=31):
                            res.append(giorno+'/'+d[mese]+'/'+'19'+anno)
                        elif(int(giorno)>40 and int(giorno)<50):
                            res.append('0'+str(int(giorno)-40)+'/'+d[mese]+'/'+'19'+anno)
                        else:
                            res.append(str(int(giorno)-40)+'/'+d[mese]+'/'+'19'+anno)
            else:
                if(mese not in d):
                    res.append('Mese errato')
                else:
                    res.append('Giorno errato')
        else:
            res.append('Codice errato')
    return res
    
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
