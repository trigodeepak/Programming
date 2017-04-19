#include <iostream>
using namespace std;
int visited[5]={0};
struct edge{
	int w;
	int a[2];
	int t=0;
};
void kuruskal(edge my[],int n){
	int i,j;
	visited[my[0].a[0]]=1;
	visited[my[0].a[1]]=1;
	my[0].t=1;
	for(i=1;i<n;i++)
	{ if(visited[my[i].a[0]]==0||visited[my[i].a[0]]==0)
		{
			visited[my[i].a[0]]=1;
			visited[my[i].a[1]]=1;
			my[i].t=1;
		}
	}
	for(i=0;i<n;i++)
	{
		if(my[i].t==1)
		{cout<<my[i].a[0]<<"--"<<my[i].a[1]<<" "<<my[i].w<<"\n";}
	}
}
int main() {
	edge my[5];
	my[0].w=4;
	my[0].a[0]=2;
	my[0].a[1]=3;
 
	my[1].w=5;
	my[1].a[0]=0;
	my[1].a[1]=3;
 
	my[2].w=6;
	my[2].a[0]=0;
	my[2].a[1]=2;
 
	my[3].w=10;
	my[3].a[0]=0;
	my[3].a[1]=1;
 
	my[4].w=15;
	my[4].a[0]=1;
	my[4].a[1]=3;
	
	kuruskal(my,5);
}
