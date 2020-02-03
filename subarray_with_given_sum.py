#!/usr/bin/env python3

"""
Given an unsorted array A, find a subarray with given sum S
"""


def subarray_with_given_sum(s, a):
    n = len(a)
    _sum = a[0]
    start = 0
    i = 1
    while i <= n:
        while _sum > s and start < i-1:
            _sum -= a[start]
            start += 1
        if _sum == s:
            return a[start:i]
        if i < n:
            _sum += a[i]
        i += 1
    return None


if __name__ == "__main__":
    A = [6, 5, 7, 8, 2, 3, 4, 15, 20]
    S = 15
    result = subarray_with_given_sum(S, A)
    if subarray_with_given_sum is not None:
        print(result)
    else:
        print("Could not find sub-array.")
