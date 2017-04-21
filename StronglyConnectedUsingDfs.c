#include<stdio.h>
#include<stdlib.h>
//DFS With dynamic allocation of the variables
//#include<iostream>
//using namespace std;
static int time = 0;
int *par,*d,*f;
int b[5][5];
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
void depth_first_strongly_connected(int n,int a[][n],int b[]){
    int i;

	for (i=0;i<n;i++){
		colour[i]='W';
		par[i]='-1';
//		printf("%d",b[i]);
	}
	for (i=n-1;i>=0;i--){
		if (colour[b[i]]=='W')
		{ printf("\nStrongly Connected are : ");
		dfs_visit(b[i],n,a);}
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
void transpose(int n,int a[][n]){
    int i,j;
//    int **b;
//    b= (int **)malloc(n*n*sizeof(int));
    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            b[i][j]=a[j][i];
}
int main()
{
      int a[5][5]= {{0,0,1,1,0},
                    {1,0,0,0,0},
                    {0,1,0,0,0},
                    {0,0,0,0,1},
                    {0,0,0,0,0}};
      int n=5;
      par = (int *)malloc(n*sizeof(int));
      d = (int *)malloc(n*sizeof(int));
      f = (int *)malloc(n*sizeof(int));
      colour = (char *)malloc(n*sizeof(char));
      printf("Depth First is :\n");
	  depth_first(n,a);
	  int i,j;
	  int array[n][2];
    for (i = 0; i < n; i++)
	{
        array[i][0] = f[i];
        array[i][1] = i;
    }

    printf("\nTopological Sort is :\n");
    qsort(array, n, sizeof array[0], compare);
    for(i = n-1;i >=0;--i)
        printf("%d\n", array[i][1]);
        transpose(n,a);
//    int **b=transpose(n,a);
//    for(i=0;i<n;i++)
//        for(j=0;j<n;j++)
//            printf("%d ",b[i][j]);
    depth_first_strongly_connected(n,b,&array[0]);

    free(par); free(f); free(d); free(colour);
return 0;
}
