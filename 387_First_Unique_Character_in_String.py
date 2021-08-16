def firstUniqChar(s):
    """
    Given a string s, 
    find the first non-repeating character in it 
    and return its index. 
    If it does not exist, return -1.
    """
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i
    return -1


if __name__ == "__main__":
    s = "loveleetcode"
    ans = firstUniqChar(s) 
    print(ans) 