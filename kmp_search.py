#!/usr/bin/env python3
"""KMP string search algorithm. Zero dependencies."""

def build_lps(pattern):
    lps = [0] * len(pattern)
    length = 0; i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1; lps[i] = length; i += 1
        elif length:
            length = lps[length - 1]
        else:
            lps[i] = 0; i += 1
    return lps

def kmp_search(text, pattern):
    if not pattern: return []
    lps = build_lps(pattern)
    matches = []; i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1; j += 1
        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j: j = lps[j - 1]
            else: i += 1
    return matches

def kmp_count(text, pattern):
    return len(kmp_search(text, pattern))

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        print(kmp_search(sys.argv[1], sys.argv[2]))
