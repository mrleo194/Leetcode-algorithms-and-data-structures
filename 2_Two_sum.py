def twoSum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if target == nums[i] + nums[j]:
                return i, j

if __name__ == "__main__":
    lst = [2, 7, 11, 15]
    target = 9
    ans = twoSum(lst, target)
    print(ans)