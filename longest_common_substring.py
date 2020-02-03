from pprint import pprint
def longest_common_substring(A, B):
    len_A = len(A)
    len_B = len(B)
    dp = [[0 for _ in range(len_B + 1)] for _ in range(len_A + 1)]
    max_length = 0
    for i in range(len_A + 1):
        for j in range(len_B + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0
    pprint(dp)
    return max_length


if __name__ == "__main__":
    A = "SomeRandomText"
    B = "SomeMoreRandomText"
    expected = 11 # eRandomText
    actual = longest_common_substring(A, B)
    if actual == expected:
        print("Passed.")
    else:
        print("Failed.")
