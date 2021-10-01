#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> v;
    int n, size;
    cin >> size;
    while(cin >> n)
        v.push_back(n);
    sort(v.begin(), v.end());
    cout << size << endl;
    for(auto i : v)
        cout << i << " ";
    return 0;
}