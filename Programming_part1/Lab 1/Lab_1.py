print('Please enter the value for N\n');
n=int(input());
s=0;
for i in range (1,n,1):
    if i % 2 == 0:
        s=s+i;
        print("\nCurrent value i=", i, "s=", s);
print("Final result suma is s=", s);