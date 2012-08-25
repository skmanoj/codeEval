#include<stdio.h>
int a[1001];

void init()
{
   int i;
   for(i=0;i<=1000;i++)
   	a[i]=0;
   a[0]=a[1]=1;
   int j=2;
   for(j=2;j<500;j++)
      for(i=j+j;i<=1000;i+=j)
      	 a[i]=1;	
}

int ispalin(int n)
{
   int tmp=0,x=n;
   while(x!=0)
   {
      int val=x%10;
      tmp=tmp*10 + val;
      x/=10;
   }
   if(n==tmp)
     return 1;
   return 0;  
}

int main()
{
  int i;
  init();
  for(i=989;i>=0;i-=2)
  {
     if(a[i]==0)
        if(ispalin(i))
           break;
  }
  printf("%d",i);
  return 0;
}

