// This is my first JavaScript program
// <script type = "text/javascript">

var n = 0;
var i = 0;
var s = 0;

document.write("Please enter value for N\n");
document.write("<br>");
n = prompt("Please enter value for N\n");
s = 0;
for (i = 1; i <= n; i += 1)
{
    if (i % 2 === 0)
    {
        s = s + i;
        document.write("Current value i = " + i + " S = " + s + "\n");
        document.write("<br>");
    }
}
document.write("Final result suma is S = " + s);

// </script>