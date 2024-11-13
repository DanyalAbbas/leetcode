#include <stdio.h>
#include <string.h>

int target = 9;

int main()

{
    int nums[] = {2,11,7,15};
    int Final[2] = {0};

    int len = sizeof(nums) / sizeof(nums[0]);
 
    for (int i = 0; i < len; i++)
    {
        for (int j = i+1; j < len; j++)
        {
            if (nums[i] + nums[j] == target)
            {Final[0] = i; Final[1] = j;}

        }
    }

    ArrayMaker(Final, 2);

}

int ArrayMaker(int arr[], int size)
{
    printf("\n{");
    for (int i = 0; i < size -1; i++)
    {
        printf("%d, ", arr[i]);
    }
    printf("%d}", arr[size-1]);
}