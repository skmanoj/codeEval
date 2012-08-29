#include<stdio.h>
#include <iostream>
#include <string.h>
#include <string>
using namespace std;

char a[10][5]={"0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
char s[10];
char soln[10];
int b[10];
bool forComma;

void sol(int n,int pos)
{
   int i;
   if(n==7 || pos==7)
   {
      if(!forComma)
         printf(",");
      forComma=false;   
      for(i=0;i<7;i++)
         printf("%c",soln[i]);
      return; 
   }
   int j=b[pos];
   for(i=0;i<strlen(a[j]);i++)
   {
      soln[n]=a[j][i];
      sol(n+1,pos+1);
   }
}

void solve()
{
  int i;
  for(i=0;i<7;i++)
    b[i]=s[i]-'0';
  forComma=true;  
  sol(0,0);
  printf("\n"); 
}


int main(int argc, char *argv[]) 
{
	char *fn=argv[1];
	freopen(fn,"r",stdin);
	while (scanf("%s",s)!=EOF) 
		solve();
	return 0;
}
