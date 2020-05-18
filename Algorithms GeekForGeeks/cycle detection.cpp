#include<stdio.h>
# include<iostream>
#include<bits/stdc++.h> 
using namespace std;
#include <vector>

class graph{
	/*int v;
	list <int> *adj;
	bool iscycleutil(int v,bool visited[],bool *rs);*/
	public:
		int v;
		list <int> *adj;
		bool iscycleutil(int v,bool visited[],bool *rs);
		graph(int v);  //constructor
		void addedge(int v, int w);
		bool iscyclic();
};
graph::graph(int v){ //:: is scope resolution method
	this->v=v;
	adj=new list<int>[v];
}
void graph::addedge(int v,int w){
	adj[v].push_back(w);   // add w to adj v's list
}
bool graph::iscycleutil(int v,bool visited[],bool recstack[]){
	if(visited[v]==false){
		visited[v]=true;
		recstack[v]=true;
	list<int>::iterator i;
	for(i=adj[v].begin();i!=adj[v].end();i++){
		if(!visited[*i] && iscycleutil(*i,visited,recstack))
			return true;
		else if(recstack[*i])
			return true;
	}	
	}
recstack[v]=false;
return false;
}
bool graph::iscyclic(){
	bool *visited=new bool[v];
	bool *recstack=new bool[v];
	for(int i=0;i<v;i++){
		visited[i]=false;
		recstack[i]=false;
	}
	for(int i=0;i<v;i++)
		if(iscycleutil(i,visited,recstack))
			return true;
	return false;
}



int main(){
	cout<<"Enter Number Of Vertices."<<endl;
	int v,s,e,l;
	cin>>v;
	graph g(v);
	cout<<"Enter Number Of Edges."<<endl;
	cin>>e;
	for(int i=0;i<e;i++){
		cin>>s>>l;
		g.addedge(s,l);
	}
	if(g.iscyclic()){
		cout<<"Cycle Found"<<endl;
	}
	else{
		cout<<"Cycle Not Found"<<endl;
	}
}
