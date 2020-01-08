
def divisors(n):
    lst = []
    for i in range(2,int(n/2)+1):
        if n % i ==0:
            lst.append(i)
    print(lst)         

    
divisors(20)