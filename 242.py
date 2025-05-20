def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    occur_s, occur_t = {}, {}

    for i in s: 
        if i in occur_s:
            occur_s[i] += 1
        else:
            occur_s[i] = 1

    for i in t: 
        if i in occur_t:
            occur_t[i] += 1
        else:
            occur_t[i] = 1
    if occur_s == occur_t:
        return True
    return False
                