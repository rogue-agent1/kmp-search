#!/usr/bin/env python3
"""kmp_search - Knuth-Morris-Pratt string search."""
import argparse

def compute_lps(pattern: str) -> list:
    lps = [0] * len(pattern)
    length, i = 0, 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1; lps[i] = length; i += 1
        elif length: length = lps[length - 1]
        else: lps[i] = 0; i += 1
    return lps

def kmp_search(text: str, pattern: str) -> list:
    if not pattern: return []
    lps = compute_lps(pattern)
    matches, i, j = [], 0, 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1; j += 1
            if j == len(pattern):
                matches.append(i - j); j = lps[j - 1]
        elif j: j = lps[j - 1]
        else: i += 1
    return matches

def main():
    p = argparse.ArgumentParser(description="KMP string search")
    p.add_argument("pattern"); p.add_argument("text", nargs="?")
    p.add_argument("-f", "--file", help="Search in file")
    args = p.parse_args()
    if args.file: text = open(args.file).read()
    elif args.text: text = args.text
    else: import sys; text = sys.stdin.read()
    matches = kmp_search(text, args.pattern)
    print(f"Pattern: '{args.pattern}'")
    print(f"Matches: {len(matches)} at positions {matches[:20]}")

if __name__ == "__main__":
    main()
