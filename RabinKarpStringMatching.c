#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
//RABIN KARP String matching algorithm, Works only if the mod of negative numbers is positive
int main()
{   char t[]="12345";
    char p[]="23";
    int n = strlen(t),m=strlen(p);
    int d=10,q=13,i,s,ph=0,th=0,f=0;
    int h=((int)pow(10,m-1))%q;
    for (i=0;i<m;i++){
        //th and ph are hash for text and pattern
        ph =(d*ph+p[i])%q;
        th = (d*th+t[i])%q;
    }
    int a = -119 % 13;
    printf("%d ",a);
    for (s=0;s<n-m;s++){
        if(ph==th)
        {   f=1;
            for (i=s;i<m+s;i++)
            { if (p[i]!=t[i])
                f=0;
                break;
            }
            if(f==1)
            {   printf("Pattern Matched at shift %d",s);
                exit(0);
            }
        }
        else {
            //The problem is here the modulus keep on being negative due to the operation of %
            th=(d*(th-t[s]*h)+t[s+m])%q;
        }
    }
    if(f==0)
        printf("The pattern is not matched");
    return 0;
}
