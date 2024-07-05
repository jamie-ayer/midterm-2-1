import random

def split(nums):
    
    pivot = nums.pop()
    lowL = []
    hiL = []
    
    while nums:
        if nums[0] <= pivot:
            lowL.append(nums.pop(0))
        else:
            hiL.append(nums.pop(0))
    
    lowL.append(pivot)
    nums += lowL
    nums += hiL
    
    return pivot

def main():
    
    nums = [random.randint(1,50) for x in range(10)]
    print(f'List before split: {nums}')
    pivot = split(nums)
    print(f'Pivot used: {pivot}\nList after split: {nums}')
    
if __name__ == '__main__':
    main()