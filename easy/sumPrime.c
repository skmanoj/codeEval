#include<stdio.h>
int a[10001];

void init()
{
   int i;
   for(i=0;i<=10000;i++)
   	a[i]=0;
   a[0]=a[1]=1;
   int j=2;
   for(j=2;j<5000;j++)
      for(i=j+j;i<=10000;i+=j)
      	 a[i]=1;	
}

int main()
{
   init();	
   int i=0;
   long int sum=0;
   int cnt=1000;
   for(i=0;i<10000;i++)
   	if(a[i]==0)
   	{
   	   sum+=i;
   	   cnt--;
   	   if(cnt==0)
   	   	break;
   	}  
   printf("%ld",sum);	   
   return 0;		
}
