#include<stdio.h>
int main(void)
{
int n=0;
int i=0;
int s=0;
printf("Please enter value for N\n");
scanf("%d",&n);
s=0;
for(i=1;i<=n;i+=1)
    {
        if (i % 2 = 0)
            {
            s=s+i;
            printf("Current value i=%d S=%d\n", i, s);
            }
    }
printf("Final result suma is S=%d", s);
}