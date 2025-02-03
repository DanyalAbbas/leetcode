import sys

def foo(nums: list[int]) -> int:
    nums = sorted(nums)
    n = len(nums)
    if n % 2 == 1:
        median = nums[n // 2]
    else:
        median = (nums[n // 2 - 1] + nums[n // 2]) // 2
    return median

if __name__ == "__main__":
    numbers = []
    
    for line in sys.stdin:  
        num = int(line.strip()) 
        numbers.append(num)  
        print(foo(numbers))  