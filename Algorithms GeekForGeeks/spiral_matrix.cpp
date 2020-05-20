#include<iostream>
using namespace std;

void plus_x(int **mat,int start,int end,int row,int col){//correct
	//cout<<"in plus_x at "<<start<<" "<<end<<endl;
	for(int i=start;i<=col-1-start;i++){
		cout<<mat[start][i]<<" ";
	}
}
void minus_y(int **mat,int start,int end,int row,int col){//correct
	//cout<<"in minus_y at "<<start<<" "<<end<<endl;
	for(int i=start;i<=row-start;i++){
		cout<<mat[i][end]<<" ";
	}
}
void minus_x(int **mat,int start,int end,int row,int col){//correct
	//cout<<endl<<"in minus_x at "<<start<<" "<<end<<endl;
	//cout<<end<<","<<row-1-start<<endl;
	for(int i=end;i>=row-1-start;i--){
		cout<<mat[start][i]<<" ";
		//cout<<"("<<start<<","<<i<<") ";
	}
}
void plus_y(int **mat,int start,int end,int row,int col){
	//cout<<"in plus_y at "<<start<<" "<<end<<endl;
	for(int i=start;i>=row-start-1;i--){
		cout<<mat[i][end]<<" ";
	}
}
void print_spiral_matrix(int **mat,int row,int col){
	int v=col/2;
	for(int i=0;i<v;i++){
		plus_x(mat,i,i,row,col);
		minus_y(mat,i+1,col-1-i,row,col);
		minus_x(mat,row-1-i,col-2-i,row,col);
		plus_y(mat,row-2-i,i,row,col);
	}
	if(row&1==1 && col&1==1)
	plus_x(mat,v,v,row,col);
}
int main(){
	int row,col;
	cin>>row>>col;
	int **mat=new int*[row];
	for(int i=0;i<row;i++){
		mat[i]=new int [col];
		for(int j=0;j<col;j++){
			cin>>mat[i][j];
		}
	}
	print_spiral_matrix(mat,row,col);
}
