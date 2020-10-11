##Code for finding gcd and lcm using Euclidean Algorithm

def gcd(x,y):
    if(x==0):
        return(y)
    return gcd(y%x,x)

    
for _ in range(int(input())):
    a, b = [int(i) for i in input().split()]
    c=gcd(a,b)
    print("gcd-",c,"lcm-",(a*b)//c)
