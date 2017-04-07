//Debugging done program working fine
#include <stdio.h>
#include <stdlib.h>
int max(int a,int b)
{   if(a>=b)
    return a;
    else
    return b;
}
int main()
{
    int n=5,w[]={2,3,4,5,9},v[]={3,4,5,8,10},m=10;
    int c[n+1][m+1],i,j;
    for(i=0;i<n+1;i++)
      for(j=0;j<m+1;j++)
        c[i][j]=0;
    for(i=0;i<n+1;i++)
    {   for(j=0;j<m+1;j++)
        {   if(i==0||m==0)
                c[i][j]=0;
            else if(w[i-1]>j)
                c[i][j]=c[i-1][j];
            else if(i>0&&w[i-1]<=j)
                c[i][j]=max(v[i-1]+c[i-1][j-w[i-1]],c[i-1][m]);
        }
    }
    for(i=0;i<n+1;i++)
      {for(j=0;j<m+1;j++)
    printf("%d ",c[i][j]);
    printf("\n");}
    return 0;
}
