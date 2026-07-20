def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            print("it is not a prime number")
    print("it is a prime number")
n=int(input("enter the number"))
prime(n)
        
