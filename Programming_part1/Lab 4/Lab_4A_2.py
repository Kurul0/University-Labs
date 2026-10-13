import math;
x=y=A=B=dx=float();
print ("Please, enter the start point A\n")
A=float(input());
print ("Please, enter the end point B\n")
B=float(input());
print ("Please, enter the step dx\n")
dx=float(input());
x=A;
while True:
    if x!=0:
        y=math.log(abs(x), 2);
        print (f'x={x:10.3f} y={y:10.3f}');
    else:
        print (f'x={x:10.3f} y= ERROR: could not calculate')
    x=x+dx;
    if x>B:
        break;