#include <bits/stdc++.h>
using namespace std;


int foo(vector<string>& tokens) 
{
    vector<int> stack;
    for (string token : tokens)
    {
        if (token == "+" || token == "-" || token == "*" || token == "/")
        {
            int b = stack.back(); stack.pop_back();
            int a = stack.back(); stack.pop_back();
            if (token == "+") stack.push_back(a + b);
            else if (token == "-") stack.push_back(a - b);
            else if (token == "*") stack.push_back(a * b);
            else if (token == "/") stack.push_back(a / b);
        }
        else
        {
            stack.push_back(stoi(token));
        }
    }
    return stack[0];

}