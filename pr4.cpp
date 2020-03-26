#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two n-digit numbers where n is a nnumber entered by user.
#include <iostream>
using namespace std;
int largestPalindromeofN(int num)
{
    int n, prod, m = 0, pm=0;
    for (int i = 1; i <= num; i++)
    {
        m *= 10;
        m += 9;
    }
    n = 1 + m / 10;
    pm = 0;
    for (int i = m; i >= n; i--)
    {
        for (int j = i; j >= n; j--)
        {
            prod = i * j;
            if (prod < pm)
                break;
            int number = prod, rev = 0;
            while (number != 0)
            {
                rev = rev * 10 + number % 10;
                number /= 10;
            }
            if (prod == rev && prod > pm)
                pm = prod;
        }
    }
    return pm;
}
int main()
{
    int n;
    cin>>n;
    cout << largestPalindromeofN(n);
    return 0;
}
