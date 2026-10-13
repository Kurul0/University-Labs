import math;
K = 0.0186;
L = 0.01;
x=y=a=b=float();
print('Please enter the value of x:');
x = float(input());
a=(4-math.pow(K,2))/(math.sqrt(L)*math.sqrt(100*L))*(math.sin(x)/math.cos(x));
print('Result of a:', a);
b=math.pow(math.sin(10*L+math.exp(1/3*math.log(math.log10(x)))), 4);
print('Result of b:', b);
if (math.pow(a,2)+math.pow(b,2))>10:
    y=math.sqrt(abs(a-b));
else:
    y=a+b;
print('Result of y:', y);