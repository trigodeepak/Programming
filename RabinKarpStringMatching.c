#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
//RABIN KARP String matching algorithm
int positive_modulo(int i, int n) {
    return (i % n + n) % n;
}
int main()
{   char t[]="12345";
    char p[]="23";
    int n = strlen(t),m=strlen(p);
    int d=10,q=13,i,s,ph=0,th=0,f=0,k;
    int h=((int)pow(10,m-1))%q;
    for (i=0;i<m;i++){
        //th and ph are hash for text and pattern
        ph =positive_modulo(d*ph+p[i],q);
        th = positive_modulo(d*th+t[i],q);
    }
    for (s=0;s<n-m;s++){
        if(ph==th)
        {   f=1;
            k=0;
            for (i=s;i<m+s;i++)
            { if (p[k++]!=t[i])
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
            th=positive_modulo((d*(th-t[s]*h)+t[s+m]),q);
        }
    }
    if(f==0)
        printf("The pattern is not matched");
    return 0;
}
