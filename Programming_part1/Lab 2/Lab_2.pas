Program Lab2A (Input, Output);
const
K=2;
var
W:real;
X:real;
y1, y2, y3, y4, y5, y6:real;
begin
writeln('Please enter the value of X');
readln(X);
y1:=exp (-3*ln(7.3910));
y2:=y1*X;
y3:=exp (5*ln(X));
y4:=exp (1/K);
y5:=y4-1;
y6:=y3*y5;
W:=y2/y6;
writeln ('Result is W=', W);
end.