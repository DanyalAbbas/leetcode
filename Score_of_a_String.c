#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{

    printf("%d", StringScore("hello"));

}

int StringScore(char s[])
{
    int length = strlen(s);
    int added = 0;

    for (int i = 0; i < length-1; i++)
    {
        added += abs(s[i] - s[i+1]);
    }

    return added;
}