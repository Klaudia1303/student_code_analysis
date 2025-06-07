def A_Ex8(fileName):
    f=open(fileName,"r",encoding="utf-8")
    max_alpha_ch_num=0
    row=0
    
    for idx, line in enumerate(f.readlines()):
        alpha_chars_num=0
        
        for ch in line:
            if ch.isalpha() and ch.isupper():
                alpha_chars_num += 1
        
        if alpha_chars_num>max_alpha_ch_num:
            max_alpha_ch_num = alpha_chars_num
            row= idx + 1
        if alpha_chars_num == max_alpha_ch_num:
            row= max(row,idx+1)
            
    f.close()
    
    return row
    
    

    
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, ["file1.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file2.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file3.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file4.txt"] , 3)
    counter_test_positivi += tester_fun(A_Ex8, ["file5.txt"] , 3)

    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
