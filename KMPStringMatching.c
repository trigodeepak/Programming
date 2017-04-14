#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
//KMP Matching algorithm
int * ComputePrefix(char *a)
{   int m = strlen(a);
    int pi[m+1];
    pi[0]=0;
    int k=0,q;
    for(q=1;q<m;q++){
        while (k>0&&a[k]!=a[q-1])
            k=pi[k];
        if(a[k]==a[q-1])
            k++;
        pi[q]=k;
    }
    return pi;
}
int main()
{   char t[]="12345";
    char p[]="aabaabaaa";
    int *pi = ComputePrefix(p);//The function is not working properly since the indexing have some problem
    int m = strlen(p);
    int i;
    for (i=0;i<m;i++)
        printf("%d ",pi[i]);
    return 0;
}
