"""
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def longest_substring(s):
    if not s:
        return 0
    max_length = 1
    cur_length = 1
    visited = {s[0]: 0}
    for i in range(1, len(s)):
        prev_index = visited.get(s[i], -1)
        if prev_index == -1 or (i-cur_length > prev_index):
            cur_length += 1
        else:
            if cur_length > max_length:
                max_length = cur_length
            cur_length = i-prev_index
        visited[s[i]] = i
    if cur_length > max_length:
        max_length = cur_length
    return max_length


if __name__ == "__main__":
    TESTS = {
        "abcabcbb": 3,
        "bbbbb": 1,
        "pwwkew": 3
    }
    for s, expected in TESTS.items():
        actual = longest_substring(s)
        if expected == actual:
            print("Passed.")
        else:
            print("Failed. Expected = {}, Actual = {}".format(expected, actual))
