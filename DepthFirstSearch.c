#include<stdio.h>
#include<stdlib.h>
static int time = 0;
int par[5],d[5],f[5];
char colour[5][1];
void dfs_visit(int i,int **a,int n){
	colour[i][0]='G';
	time++;
	d[i]=time;
	for (j=0;j<n&&j!=i;j++){
		if (a[i][j]==1){
			if(colour[j][0]=='W'){
				par[j]=i+1;
				dfs_visit(j,a,n);
			}
		}
	}
	colour[i][0]='B';
	f[i]=++time;
}
void depth_first(int **a,int n){
	int i;
	
	for (i=0;i<n;i++){
		colour[i][0]='W';
		par[i]='-1';			
	}
	for (i=0;i<n;i++){
		if (colour[i][0]=='W')
		{ dfs_visit(i,a,n);}
	}
}
int main()
{
//      FILE *fp;
      int n=5;
      int a[5][5]= {{0,1,0,0,1},{1,0,1,1,0},{0,1,0,0,1},{0,1,1,0,1},{1,1,0,1,0}};
	  depth_first(a,n);
return 0;
}
