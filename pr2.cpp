#include <bits/stdc++.h>
using namespace std;
int main(){
	int a=0,b=1,c=0;
	int n,ans=0,i=1;
	cin>>n;
	if(n==1){
		cout<<0<<endl;
		return 0;
	}
	while(c<n){
		if(i%2==0){
			ans+=c;
// 			cout<<c<<endl;
		}i++;
		c=a+b;
		a=b;b=c;
	}
	cout<<ans<<endl;
	return 0;
}
