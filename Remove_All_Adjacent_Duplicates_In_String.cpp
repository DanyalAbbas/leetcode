#include <bits/stdc++.h>
using namespace std;

string foo(string s) 
{
    vector<char> stack;
    for (char i : s)
    {
        if (!stack.empty() && stack.back() == i)
        {
            stack.pop_back();
        }
        else
        {
            stack.push_back(i);
        }
        
    }
    return string(stack.begin(), stack.end());
    
    
}