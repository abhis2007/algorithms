#abhishek kumar
#pre-computation of prime number 
#using Sieve of Eratosthenes

import math as mt
MAXN=100001
mpf=[i for i in range(MAXN)]

def sieve():
  p=2
  while(p<=mt.ceil(mt.sqrt(MAXN))):
    if(mpf[p]==p):
      for j in range(p**2,MAXN,p):
        if(mpf[j]==j):
          mpf[j]=p
    p+=1
  return mpf

#IT WILL TAKE O(LOGN) TIME FOR PRE-COMPUTATION OF PRIME LIST
#mpf=minimum prime factor
sieve()

#GENERATING PRIME FACTOR
def primefactorisation(p):
  lists=[]
  while(p!=1):
    lists.append(mpf[p])
    p//=mpf[p]
  return(lists)


print(primefactorisation(18))




  
  
