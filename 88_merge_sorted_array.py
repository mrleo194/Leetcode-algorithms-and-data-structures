def merge_list(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while k >= 0:
        if i < 0:
            nums1[k] = nums2[j]
            j -= 1
        elif j < 0:
            nums1[k] = nums1[i]
            i -= 1
        elif nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1 



if __name__ == "__main__":
    nums1 = [1,2,3,4,5,0,0,0]
    m = 5
    nums2 = [2,5,6]
    n = 3
    ans = merge_list(nums1, m, nums1, n)
    print(ans)