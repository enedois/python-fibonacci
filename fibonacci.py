def fibonacci(jumps):
    fibo_seq=[]
    for i in range(jumps):        
        if i>=2:
            newnumber = fibo_seq[len(fibo_seq)-1] + fibo_seq[len(fibo_seq)-2]
            print(newnumber)
            fibo_seq.append(newnumber)
        else:
            print(i)
            fibo_seq.append(i)



fibonacci(100)