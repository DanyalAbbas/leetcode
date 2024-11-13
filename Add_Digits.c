#include<stdio.h>

int Add_digit(int num);

int main()
{
    printf("%d", Add_digit(38));
}

int Add_digit(int num)
{
    int add = 0;
    while (1)
    {
        while (num > 0)
        {
            add += num%10;
            num /= 10;
        }
        if (add < 10)
            break;
        num = add;
        add = 0;

    }
    return add;
}