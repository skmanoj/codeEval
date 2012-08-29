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
       {
          if(line[i]>='a' && line[i]<='z')
             c[line[i]-'a']++;
          else if(line[i]>='A' && line[i]<='Z')
             c[line[i]-'A']++;
       }   
       int tmp=0;
       for(i=0;i<26;i++)
       {
           if(c[i]==0)
           {
              tmp=1;
              printf("%c",'a'+i);
            }  
       }
       if(tmp==0)
         printf("NULL");
       printf("\n");   
   }
   return 0;
}
