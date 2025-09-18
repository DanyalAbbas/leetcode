#include <bits/stdc++.h>
using namespace std;

bool foo(string s) 
{
    vector<char> stack;
    for (char i : s)
    {
        if (i == '(' || i == '{' || i == '[') 
        {
            stack.push_back(i);
        } 
        else 
        {
            if (stack.empty()) return false;
            char top = stack.back();
            stack.pop_back();
            if ((i == ')' && top != '(') || 
                (i == '}' && top != '{') || 
                (i == ']' && top != '[')) 
            {
                return false;
            }
        }
    }
    return stack.empty();
}

int main()
{
    string s[3] = {"{[]}",  "()", "(]"};
    for (int i = 0; i < 3; i++) 
    {
        cout << foo(s[i]) << endl;
    }
}