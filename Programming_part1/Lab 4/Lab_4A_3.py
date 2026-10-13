import math;
x=y=A=B=dx=float();
i=k=int();
print ("Please, enter the start point A\n")
A=float(input());
print ("Please, enter the end point B\n")
B=float(input());
print ("Please, enter the step dx\n")
dx=float(input());
k=math.trunc((B-A)/dx)+1;
x=A;
for i in range (0,k,1):
    if x!=0:
        y=math.log(abs(x), 2);
        print (f'x={x:10.3f} y={y:10.3f}');
    else:
        print (f'x={x:10.3f} y= ERROR: could not calculate')
    x=x+dx;