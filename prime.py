n=int(input("Enter a Number:"));
prime=0;
for i in range(2, n//2+1):
    if(n%i==0):
        prime=1;
        break;
    
if prime==0:
    print(n,"is prime")
else:
    print(n, "is not prime")    
            