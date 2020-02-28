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
  
sieve()
print(mpf[:16])

def odd(n):
  if(n%2!=0):
    return 1

def politness_primefactor(n):
  lists=[]
  l=[]
  while(n!=1):
    if odd(mpf[n]):
      lists.append(mpf[n])
    n//=mpf[n]
  while(len(lists)!=0):
    l.append(lists.count(lists[0])+1)
    val=lists[0]
    for i in range(len(lists)):
      if val in lists:
        lists.remove(val)
  return l


for __ in range(int(input())):
  prod=1
  n=politness_primefactor(int(input()))
  for i in range(len(n)):
    prod*=n[i]
  print(prod-1)
  
#devsupport@paytm.com


