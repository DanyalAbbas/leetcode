#include <stdio.h>

int main()
{
    int list[] = {1,2,3,4};
    int list_size = 4;
    printf("%d", getConcatenation(list, list_size));
}

int *getConcatenation(int *arr, int arrSize)
{
    int new_arr[2*arrSize];
    int count = 0;
    for (int i = 0; i < 2*arrSize; i++)
    {
        if (count == arrSize)
            count = 0;
        
        new_arr[i] = arr[count];
        count++;
        
    }

    return new_arr;

}