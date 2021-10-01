#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n, i, num, p, a, b;
    vector<int> v;
    cin >> n;
    for(i = 0; i < n; i++)
    {
        cin >> num;
        v.push_back(num);
    }
    cin >> p;
    cin >> a >> b;
    v.erase(v.begin() + p - 1);
    v.erase(v.begin() + a - 1, v.begin() + b - 1);
    cout << v.size() << endl;
    for(auto i : v)
    {
        cout << i << " ";
    }
    return 0;
}