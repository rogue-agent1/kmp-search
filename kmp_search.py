#!/usr/bin/env python3
"""kmp_search — Knuth-Morris-Pratt string matching. Zero deps."""

def build_lps(pattern):
    lps = [0] * len(pattern)
    length, i = 0, 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length:
            length = lps[length - 1]
        else:
            i += 1
    return lps

def kmp_search(text, pattern):
    if not pattern:
        return list(range(len(text) + 1))
    lps = build_lps(pattern)
    matches = []
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                matches.append(i - j)
                j = lps[j - 1]
        elif j:
            j = lps[j - 1]
        else:
            i += 1
    return matches

def main():
    text = "AABAACAADAABAABA"
    pattern = "AABA"
    lps = build_lps(pattern)
    matches = kmp_search(text, pattern)
    print(f"Text:    {text}")
    print(f"Pattern: {pattern}")
    print(f"LPS:     {lps}")
    print(f"Matches at positions: {matches}")
    for pos in matches:
        print(f"  {' '*pos}{pattern}")

if __name__ == "__main__":
    main()
