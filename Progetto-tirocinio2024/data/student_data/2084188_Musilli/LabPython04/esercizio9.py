n=int(input("Inserire numero per continuare la successione di Fibonacci: "))
app=0; app2=1; i=0
while i<n-1:
    if app==0:  app=1; print("\t",app,"\n\t", app2)
    else:   s=app+app2; print("\t", s); app=app2; app2=s
    i+=1    
