//prgram for activity selection
#include <stdio.h>
#include <stdlib.h>
int main()
{
    int n=10,s[]={1,3,2,4,8,7,9,11,9,12},f[]={3,4,5,7,9,10,11,12,13,14};
    int m=1,i,j;
    j=0;
    for(i=1;i<n;i++)
        if(s[i]>=f[j])
            {m++; j=i;}
    printf("%d ",m);
    return 0;
}
