#!/usr/bin/env python3
"""kmp_search - Knuth-Morris-Pratt string matching algorithm."""
import sys

def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp(text, pattern):
    if not pattern:
        return []
    lps = build_lps(pattern)
    results = []
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            results.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return results

def test():
    assert kmp("ABABDABACDABABCABAB", "ABABCABAB") == [10]
    assert kmp("aaaaaa", "aa") == [0, 1, 2, 3, 4]
    assert kmp("hello world", "xyz") == []
    assert kmp("abcabc", "abc") == [0, 3]
    lps = build_lps("AABAACAABAA")
    assert lps == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
    print("OK: kmp_search")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        print("Usage: kmp_search.py test")
