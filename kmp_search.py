#!/usr/bin/env python3
"""KMP string search algorithm."""
import sys

def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length, i = 0, 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps

def kmp_search(text, pattern):
    if not pattern: return []
    n, m = len(text), len(pattern)
    lps = build_lps(pattern)
    results, i, j = [], 0, 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1; j += 1
        if j == m:
            results.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j: j = lps[j - 1]
            else: i += 1
    return results

def test():
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [10]
    assert kmp_search("aaaaaa", "aa") == [0,1,2,3,4]
    assert kmp_search("hello world", "xyz") == []
    assert kmp_search("abcabc", "abc") == [0, 3]
    assert build_lps("ABABCABAB") == [0,0,1,2,0,1,2,3,4]
    print("  kmp_search: ALL TESTS PASSED")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else: print("KMP string search")
