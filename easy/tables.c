#include<stdio.h>
int main()
{
   int i=1,j=1;
   for(i=1;i<=12;i++)
   {
      for(j=1;j<=11;j++)
        printf("%4d",i*j);
      printf("%4d\n",i*j);  
   }
   return 0;
}
