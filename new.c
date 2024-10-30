#include <stdio.h>

int main()
{
    int nums[] = {2,7,11,15};
    int target = 9;
    int arr[2];

    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (nums[i] + nums[j] == target)
            {
                arr[0] = i;
                arr[1] = j;
            }
        }
    }

    ArrayMaker(nums, 4);
    ArrayMaker(arr, 2);

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