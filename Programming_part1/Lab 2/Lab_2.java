import java.util.*;
import java.lang.*;
import java.io.*;

public class MyLab2
{
    public static void main (String[] args) throws java.lang.Exception
    {
        double x=0.0;
        final double k=2;
        final double e=Math.E;
        double w=0.0;
        double y1,y2,y3,y4,y5,y6;
        System.out.println("Please enter the value of x\n");
        Scanner in = new Scanner(System.in);
        x = in.nextDouble();
        in.close();
        y1=Math.pow (7.3910, -3);
        y2=y1*x;
        y3=Math.pow (x, 5);
        y4=Math.pow (e, 1/k);
        y5=y4-1;
        y6=y3*y5;
        w=y2/y6;
        System.out.print ("Result is w="+w);
    }
}