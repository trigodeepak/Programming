//Program for bfs in graph working correctly
#include<stdio.h>
#include<iostream>
#include<stdlib.h>
static int time = 0;
int inf = 99999;
int par[5],d[5];
char colour[5][1];
int que[5];
int k=0;int f=0;
void bfs(int a[][5],int n,int s)
{   int i,j;
    for (i=0;i<n;i++){
    colour[i][0]='W';
    d[i]=inf;
    par[i]=-1;
    }
    colour[s][0]='G';
    d[s]=0;
    par[s]=-1;
    que[k++]=s;
    while(k>f){
        int u = que[f++];
        printf("%d ",u);
        for(j=0;j<n;j++){
		if (a[u][j]==1){
			if(colour[j][0]=='W'){
				colour[j][0]='G';
                d[j]=d[u]+1;
                par[j]=u;
                que[k++]=j;
                }
            }
        }
	colour[u][0]='B';
    }
//    printf("\n");
//    for (i=0;i<5;i++)
//        printf("%d ",que[i]); //To print the contents of queue

}
int main()
{
      int n=5;
      int a[5][5]= {{0,1,0,0,1},{1,0,1,1,0},{0,1,0,0,1},{0,1,1,0,1},{1,1,0,1,0}};
	  bfs(a,n,4);
return 0;
}
