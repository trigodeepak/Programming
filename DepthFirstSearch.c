#include<stdio.h>
#include<stdlib.h>
//DFS With dynamic allocation of the variables
//#include<iostream>
//using namespace std;
static int time = 0;
int *par,*d,*f;
char *colour;
void dfs_visit(int i,int n,int a[][n]){
	colour[i]='G';
	time++;
	d[i]=time;
	int j;
	printf("%d ",i);
	for (j=0;j<n;j++){
		if (a[i][j]==1){
			if(colour[j]=='W'){
				par[j]=i+1;
				dfs_visit(j,n,a);
			}
		}
	}
	colour[i]='B';
	f[i]=++time;
}
void depth_first(int n,int a[][n]){
	int i;

	for (i=0;i<n;i++){
		colour[i]='W';
		par[i]='-1';
	}
	for (i=0;i<n;i++){
		if (colour[i]=='W')
		{ dfs_visit(i,n,a);}
	}
}
int compare ( const void *pa, const void *pb )
{
    const int *a = pa;
    const int *b = pb;
    if(a[0] == b[0])
        return a[1] - b[1];
    else
        return a[0] - b[0];
}
int main()
{
//      FILE *fp;
      int n=5;
      int a[5][5]= {{0,1,0,0,1},{1,0,1,1,0},{0,1,0,0,1},{0,1,1,0,1},{1,1,0,1,0}};
      par = (int *)malloc(n*sizeof(int));
      d = (int *)malloc(n*sizeof(int));
      f = (int *)malloc(n*sizeof(int));
      colour = (char *)malloc(n*sizeof(char));
      printf("\n Depth First is :\n");
	  depth_first(n,a);
//	  int i;
//	  int array[n][2];
//    for (i = 0; i < n; i++)
//	{
//        array[i][0] = f[i];
//        array[i][1] = i;
//    }
//
//    printf("\n Topological Sort is :\n");
//    qsort(array, n, sizeof array[0], compare);
//    for(i = n-1;i >=0;--i)
//        printf("%2d\n", array[i][1]);
    free(par); free(f); free(d); free(colour);
return 0;
}
