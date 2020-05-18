#include<stdio.h>
#include<stdlib.h>
#include<stack>
#include<iostream>
using namespace std;
void topological_sort_util(int **adj,bool *visited,stack<int>&restack,int n,int i){
	visited[i]=true;
	for(int v=0;v<n;v++){
		if(adj[i][v]==1 && !visited[v])
		topological_sort_util(adj,visited,restack,n,v);
	}
	restack.push(i);
}

void topo_sort(int **adj,int n){
	bool *visited=new bool[n];
	for(int i=0;i<n;i++)
		visited[i]=false;
	stack <int> restack;
	for(int i=0;i<n;i++){
		if(!visited[i])
		topological_sort_util(adj,visited,restack,n,i);
	}
	while(!restack.empty()){
		cout<<restack.top()<<" ";
		restack.pop();
	}
}

int main(){
	int v,s,end,e;
	cout<<"Enter Number Of Vertices"<<endl;
	cin>>v;
	cout<<"Enter number of edges"<<endl;
	cin>>e;
	int** adj=new int*[v];
	for(int i=0;i<v;i++){
		adj[i]=new int[v];
		for(int j=0;j<v;j++){
			adj[i][j]=0;
	}
	}
	for(int i=0;i<e;i++){
		cin>>s>>end;
		adj[s][end]=1;
	}
	topo_sort(adj,v);
}
