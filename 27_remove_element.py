def removeElement(nums, val):
    # create a new array with initial index j, assign in-valid element
    # in array nums (nums != val) to the new array <-> remove element  
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j


if __name__ == "__main__":
    lst = [0,1,2,2,3,0,4,2]
    #lst.remove(lst[1])
    #print(lst)
    ans = removeElement(lst, 2)
    print(ans)