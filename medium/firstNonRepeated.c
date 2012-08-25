#include<stdio.h>
#include<string.h>
int main(int argc, char *argv[] )
{
   char line[1024];
   FILE *file = fopen( argv[1], "r" );
   while(fgets(line,1024,file))
   {
       int c[26];
       int i=0;
       for(i=0;i<26;i++)
          c[i]=0;
       for(i=0;i<strlen(line);i++)
          c[line[i]-'a']++;
       for(i=0;i<strlen(line);i++)
       {
           if(c[line[i]-'a']==1)
           {
               printf("%c\n",line[i]);
               break;
           }
       }    
   }
   return 0;
}
