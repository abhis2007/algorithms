import math
MAXN=101
lists_prime=[]
prime=[i for i in range(MAXN)]
def precompute():
    p=2
    for i in range(p,math.ceil(math.sqrt(MAXN)),1):#p<=sqrt(n)
        if(prime[i]==i):#not evaluated yet
            for j in range(i*i,MAXN,i):
                if(prime[j]==j):
                    prime[j]=i
    for i in range(2,MAXN):
        if(prime[i]==i):
            lists_prime.append(i)
    return lists_prime

def EulerTotient(n):
    precompute()
    i=0
    gcd_sum=1
    while(lists_prime[i]<=n):
        p=lists_prime[i]
        if(n%p==0):
            gcd_sum*=(1-(1/lists_prime[i]))
        i+=1
    return int(gcd_sum*n)
while(1):
    print(EulerTotient(int(input("Enter Value Of N"))))
    
    
                
        





























"""def phi(n) :
    result = n
    p = 2
    while(p * p<= n) :
        if (n % p == 0) :
            while (n % p == 0) :
                n = n // p
                result = result * (1.0 - (1.0 / (float) (p))) 
	p = p + 1
	if (n > 1) :
            result = result * (1.0 - (1.0 / (float)(n))) 
    return (int)(result) 
for n in range(1, 11) :
    print("phi(", n, ") = ", phi(n)) """
