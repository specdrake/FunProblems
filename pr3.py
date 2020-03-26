#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number n entered by user?
#SOLVED



#include<bits/stdc++.h>
using namespace std;

bool IfPrime(int n) 
{ 
    if (n <= 1) 
        return false; 
    if (n <= 3) 
        return true; 

    if (n % 2 == 0 || n % 3 == 0) 
        return false; 
  
    for (int i = 5; i * i <= n; i = i + 6) 
        if (n % i == 0 || n % (i + 2) == 0) 
            return false; 
  
    return true; 
}

int LargestPrimeFactor(int n)
{
	int Largest = INT_MIN;
	for(int i=2 ; i<=n ; i++)
	{
		if(n%i == 0 && IfPrime(i) && i>Largest)
		{
			Largest = i; 
		}
	}

	return Largest;
}

int main(int argc, char const *argv[])
{
	int n;

	cin>>n;

	cout<<LargestPrimeFactor(n)<<endl;
	return 0;
}

