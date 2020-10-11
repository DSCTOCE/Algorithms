## 0/1 Knapsack problem 

W = int(input("Enter w "))
wt = [int(i) for i in input("Enter weights ").split()]
val = [int(i) for i in input("Enter values ").split()]
n = len(val)
k = [[0 for x in range(W+1)] for x in range(n+1)]
for i in range(n+1):
    for w in range(W+1):
        if i == 0 or w == 0:
            k[i][w] = 0
        elif wt[i-1] <= w:
            k[i][w] = max(val[i-1]+k[i-1][w-wt[i-1]], k[i-1][w])            
        else:
            k[i][w] = k[i-1][w]
print(k[n][W])
      
