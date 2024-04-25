#include <iostream>
#include <math.h>

using namespace std;

double LHS(double p) { return (log(1.0 - p)); }

double RHS(int k) { return ((365.5 - k) * log(365.0 / (365.0 - k)) - k); }

int FindK(double p)
{
    double lhs = LHS(p);
    for (int k = 1; k <= 366; ++k)
    {
        double rhs = RHS(k);
        if (lhs > rhs)
        {
            return k;
        }
    }
    return -1;
}

int main()
{
    double p;
    cout << "Enter the value of p: ";
    cin >> p;
    while ((p < 0 || p > 1))
    {
        cout << "Invalid input!!" << endl;
        cout << "Enter the value of p: ";
        cin >> p;
    }
    int k;

    k = FindK(p);

    if (p == 0)
        k = 1;
    else if (p == 1)
        k = 366;

    cout << "Minimum k such that probability is atleast " << p << " is " << k
         << endl;

    return 0;
}
