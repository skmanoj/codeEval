#include<stdio.h>
#include<string.h>
int main(int argc, char *argv[] )
{
   char line[1024];
   FILE *file = fopen( argv[1], "r" );
   while(fgets(line,1024,file))
   {
       int c[26];
       int i=0,len;
       for(i=0;i<26;i++)
          c[i]=0;
       len=strlen(line);
       for(i=len-1;i>=0;i--)
       {
          if(line[i]==',')
          {
            len=i;
            break;
          }  
          c[line[i]-'a']+=1;
       }  
       for(i=0;i<len;i++)
       {
          if(line[i]>='a' && line[i]<='z')
          {
            if(c[line[i]-'a'] !=0)
               continue;
          }
            printf("%c",line[i]);     
       }
      printf("\n");       
   }
   return 0;
}
