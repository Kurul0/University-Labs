using System;
//using System.Math;
public class MyLab
{
    public static void Main()
    {
        double x=0.0;
        const int k=2;
        double w=0.0;
        double y1,y2,y3,y4,y5,y6;
        const double e=2.71828;
        Console.WriteLine("Please enter value for x\n");
        x=double.Parse(Console.ReadLine());
        y1=Math.Pow(7.3910, -3);
        y2=y1*x;
        y3=Math.Pow(x, 5);
        y4=Math.Pow(e, 1.0/k);
        y5=y4-1;
        y6=y3*y5;
        w=y2/y6;
        Console.WriteLine("Result is w="+w);
    }
}