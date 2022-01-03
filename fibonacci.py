def fibonacci(jumps):
    fibo_seq=[]
    for i in range(jumps):  
        #print("iteração: "+str(i))      
        if len(fibo_seq)>=2:
            #print("ultimo"+str(fibo_seq[len(fibo_seq)-1]))
            newnumber = fibo_seq[len(fibo_seq)-1] + fibo_seq[len(fibo_seq)-2]
            print(newnumber)
            fibo_seq.append(newnumber)
        else:
            print(i)
            fibo_seq.append(i)



fibonacci(100)