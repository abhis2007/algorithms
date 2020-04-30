#include<vector>
#include<iostream>
#include <bits/stdc++.h> 
using namespace std; 
#define MAX 100001

//https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

int f[MAX]={0};
int fib(int n){
	if(n==0)
	return 0;
	if(n==1 || n==2)
	return (f[n]=1);
	if(f[n])
	return f[n];
	int k=(n&1)?(n+1)/2:n/2;
	if(n&1)
	f[n]=(fib(k)*fib(k))+(fib(k-1)*fib(k-1));
	else
	f[n]=(2*fib(k-1)+fib(k))*fib(k);
	return f[n];
}
int main(){
	int n;
	cin>>n;
	cout<<fib(n);
}
