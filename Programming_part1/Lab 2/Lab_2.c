#include <stdio.h>
#include <math.h>
#define e 2.71828
int main(void)
{
    float x=0.0;
    const int k=2;
    float w=0.0;
    float y1,y2,y3,y4,y5,y6;
    printf("Please enter the value for X\n");
    scanf("%f", &x);
    y1=pow(7.3910, -3);
    y2=y1*x;
    y3=pow(x, 5);
    y4=pow(e, 1.0/k);
    y5=y4-1;
    y6=y3*y5;
    w=y2/y6;
    printf ("Result is w=%f", w);
    return 0;
}