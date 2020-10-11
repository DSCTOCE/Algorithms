//N Queens algorithm

#include<stdio.h>

#include<math.h>

int count,x[10];

void nqueens(int,int); 
void display(int,int x[]); 
int place(int,int);

int main()
{
	int n; 
	
	printf("enter no of queens\n"); scanf("%d",&n); 
	nqueens(1,n);
	
	if(count==0)
		printf("no possible solutions\n"); 
	else
		printf("no of solutions %d",count); 
             
}

void nqueens(int k,int n) 
{              
	int i,j;
	for(i=1;i<=n;i++)
	{
	    if(place(k,i))
		{
            x[k]=i;
            if(k==n)
            {
              count++;
              display(n,x);
            }
         	else
         	nqueens(k+1,n);
	    }
	}
}


void display(int n,int x[10])
{
	int i,j;
	
	char c[10][10]; 
	for(i=1;i<=n;i++)
	    for(j=1;j<=n;j++)
			c[i][j]='X';
	
	for(i=1;i<=n;i++)
		c[i][x[i]]='Q'; 
	printf("solution : %d\n", count);   
	
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
			printf("%c",c[i][j]);
		printf("\n");
	}	
	printf("\n");
}

int place(int k,int i)
{
	int j; 
    for(j=1;j<k;j++)
	{
		if(x[j]==i||(j-x[j])==k-i||(j+x[j])==k+i) 
            return 0;
	}
	return 1;
}
