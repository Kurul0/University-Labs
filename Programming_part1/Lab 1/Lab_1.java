import java.util.*;
import java.lang.*;
import java.io.*;

public class MyLabs
{public static void main (String[] args) throws java.lang.Exception
    {
        var n=0; var i=0; var s=0;
        System.out.println("Please enter value for N\n");
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        in.close();
        s=0;
        for (i = 1; i <= n; i += 1)
        {
        	if (i % 2 == 0)
        	{
        	s = s + i;
        	System.out.println
        		("Current value i="+i+"s="+s+"\n");
        	}
        }
        System.out.println ("Final result suma is s="+s);
    }
}