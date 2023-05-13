def isAnagram( s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    s = s.lower()
    t = t.lower()

    for i in range(26):
        a = 'a'
        char = bytes(a, 'utf-8')[0] + i
        count_s[char] = 0
        count_t[char] = 0
    #print(count_s)
    for x in s:
        x = bytes(x, 'utf-8')[0]
        if x not in count_s:
            count_s[x] = 0
        else:
            count_s[x] += 1
        
    for x in t:
        x = bytes(x, 'utf-8')[0]
        if x not in count_t:
            count_t[x] = 0
        else:
            count_t[x] += 1
    b = bytes('a', 'utf-8')[0]
    for i in range(b, b+26, 1 ):
        if count_s[i] != count_t[i]:
            return False
    

    #print(count_t)
    return True

s = "abcx"
t = "axcb"
isAnagram(s, t)