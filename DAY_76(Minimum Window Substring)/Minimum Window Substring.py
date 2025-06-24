from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""

    dict_t = Counter(t)
    required = len(dict_t)

    l, r = 0, 0
    formed = 0
    window_counts = {}

    ans = float("inf"), None, None

    while r < len(s):
        char = s[r]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1

        while l <= r and formed == required:
            char = s[l]

            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1

            l += 1

        r += 1
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

s = input("Enter the string s: ")
t = input("Enter the string t: ")

result = min_window(s, t)
print(f"The minimum window substring is: '{result}'")
