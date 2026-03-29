from kmp_search import kmp_search, kmp_count, build_lps
assert kmp_search("AABAACAADAABAABA", "AABA") == [0, 9, 12]
assert kmp_search("hello", "ll") == [2]
assert kmp_search("aaa", "a") == [0, 1, 2]
assert kmp_search("abc", "xyz") == []
assert kmp_search("abc", "") == []
assert kmp_count("abababab", "ab") == 4
assert build_lps("AABAAB") == [0, 1, 0, 1, 2, 3]
print("kmp_search tests passed")
