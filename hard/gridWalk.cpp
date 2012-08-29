#include <map>
#include <iostream>
#include <queue>
 
using namespace std;
 
typedef pair<int,int> pii;
 
map < pii , bool > m;
int dirx[] = {1,0,-1,0};
int diry[] = {0,1,0,-1};
 
bool check(int x,int y) {
   int sum=0;
   x=abs(x);
   y=abs(y);
   while(x) {
      sum += x%10;
      x/=10;
   }
   while(y) {
      sum += y%10;
      y/=10;
   }
   if(sum<=19) return true;
   return false;
} 
 
int main() {
     queue < pii > q;
     q.push(make_pair(0,0));
     int cnt=0;
 
     while(!q.empty()) {
       pii p= q.front();
       q.pop();
       if(m[p]) continue;
       m[p]=1;
       if(check(p.first,p.second)){
         cnt++;
          for(int j=0;j<4;j++) {
             int xx= p.first + dirx[j];
             int yy= p.second + diry[j];
             pii pp = make_pair(xx,yy);
             if(m[pp]) continue;
             q.push(make_pair(xx,yy));
          }
       }
     }
    cout<<cnt;
}
