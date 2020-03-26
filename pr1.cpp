#include <bits/stdc++.h>
using namespace std;
int main(){
	int n,ans=0,x=3;
	cin>>n;
	if(n<3){
		cout<<ans<<endl;
	}else{
		while(x<=n){
			if(x%3==0 or x%5==0){
				ans+=x;
			}
			x++;
		}
		cout<<ans<<endl;
	}
	return 0;
}