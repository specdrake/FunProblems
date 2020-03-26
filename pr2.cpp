#include <bits/stdc++.h>
using namespace std;
int main(){
	int a=1,b=2,c=0;
	int n,ans=0;
	cin>>n;
	while(c<n){
		if(c%2==0){
			ans+=c;
		}
		c=a+b;
		a=b;b=c;
	}
	cout<<ans<<endl;
	return 0;
}
