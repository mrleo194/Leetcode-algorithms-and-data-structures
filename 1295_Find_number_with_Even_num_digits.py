
def num_digits(num):
    times_devided = 1
    result = num
    while (num // 10) != 0:
        result = num / 10
        num = result
        times_devided += 1
    return times_devided

def evendigits(nums):
    cnt = 0
    for num in nums:
        digits = num_digits(num)
        #result = num // 10
        if digits % 2 == 0:
            cnt += 1 
    return cnt

if __name__ == "__main__":
    nums = [2, 57, 123, 146577]
    ans = evendigits(nums)
    print(ans)
    #ans = num_digits(588)
    #print(ans)