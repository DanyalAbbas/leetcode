#include <bits/stdc++.h>
using namespace std;

int foo(vector<string>& operations)
{
    vector<int> stack;
    for (string i : operations)
    {
        if(i == "D" || i == "C" || i == "+")
        {
            if (i == "+") stack.push_back(stack[stack.size()-2] + stack.back());
            else if (i == "C") stack.pop_back();
            else stack.push_back(stack.back() *2);
        }
        else stack.push_back(stoi(i));
    }
    return accumulate(stack.begin(), stack.end(), 0);
}