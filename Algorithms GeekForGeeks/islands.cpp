#include<stdio.h>
#include<bits/stdc++.h>
#include <iostream>
using namespace std;

void printm(int **mat,int row,int col){
	cout<<"--------matrix---------------"<<endl;
	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++){
			cout<<mat[i][j]<<" ";
		}
		cout<<endl;
	}
	cout<<"-------------------"<<endl;
	return;
}
void check(int **mat,int x,int y,int row,int col){
	if((x>=0 && y>=0) && (y<col && x<row)){
		//cout<<"x->"<<x<<",y->"<<y<<endl;
		if(mat[x][y]==1){
			mat[x][y]=2;
			check(mat,x-1,y,row,col);//For Up
			check(mat,x+1,y,row,col);//For Down
			check(mat,x,y-1,row,col);//For Left
			check(mat,x,y+1,row,col);//For right
		}
		else
			return;
	}
	else
		return;
}
void CalNumIslands(int **mat,int row,int col){
	int island=0;
	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++){
			//printm(mat,row,col);
			if(mat[i][j]==1){
			island+=1;
			check(mat,i,j,row,col);
			}
		}
	}
	cout<<"Num Of Island:- "<<island;
}
int main(){
	int row,v,col;
	cin>>row;
	cin>>col;
	int **mat=new int*[row];
	for(int i=0;i<row;i++){
		mat[i]=new int[col];
		for(int j=0;j<col;j++){
			cin>>v;
			mat[i][j]=v;
		}
	}
	CalNumIslands(mat,row,col);
}
