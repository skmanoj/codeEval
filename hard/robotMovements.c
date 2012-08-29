#include<stdio.h>
#include<malloc.h>

int fun(int **a,int row,int col)
{
    if(row==3 && col==3)
		return 1;
	else if(row > 3 || row < 0 || col > 3 || col <0)	
		return 0;
	else if ( a[row][col]==-1)
		return 0;
	int i=0;
	int cnt=0;
	for(i=0;i<4;i++)
	{
		a[row][col]=-1;
		switch(i)//0=l,1=R,2=U,3=B
		{
			case 0:
				cnt+=fun(a,row,col-1);
				break;
			case 1:
				cnt+=fun(a,row,col+1);
				break;
			case 2:
				cnt+=fun(a,row-1,col);
				break;
			case 3:
				cnt+=fun(a,row+1,col);
				break;
		}
	}
	a[row][col]=0;
	return cnt;	
}


int main()
{
	int i=0,j=0;
	int **a;
	a=(int **)malloc(sizeof(int*)*4);
	for(i=0;i<4;i++)
		a[i]=(int *)malloc(sizeof(int)*4);
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			a[i][j]=0;
	printf("%d",fun(a,0,0));
	return 0;
}

