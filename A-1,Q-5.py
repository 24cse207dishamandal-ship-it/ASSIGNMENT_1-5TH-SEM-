def greater(a,b,c):
    if(a>b and a>c):
        print(a,"is the greatest")
    elif(b>a and b>c):
        print(b,"is the greatest")
    elif(c>b and c>a):
        print(c,"is the greatest")
    else:
        print("same value")
a=int(input("enter value for a:"))
b=int(input("enter value for b:"))
c=int(input("enter value for c:"))
greater(a,b,c)
