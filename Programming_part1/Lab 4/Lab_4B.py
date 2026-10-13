import math;
S=Si=y=x=eps=A=V=float();
i=j=int();
while True:
    print("Please, enter the value of X\n");
    x=float(input());
    if x<=1:
        break;
    else:
        print("ERROR: x is not valid")
        continue;
print("Please, enter the value of eps\n");
eps=float(input());
i = -1;
j = 4;
Si = x/4
S = 1+Si
while abs(Si)>eps:
    i = i+4
    j = j+4
    Si = Si*(-1)*(i/j)*x
    S = S+Si
y=math.pow(1+x, 1/4);
A = abs(y-S);
V = A/abs(y)*100;
print (f'y={y:10.6f} S={S:10.6f}');
print (f'A={A:8.5f} V={V:8.5f}%');