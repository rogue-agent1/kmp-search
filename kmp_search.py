#!/usr/bin/env python3
"""KMP string matching algorithm."""
import sys
def kmp_table(pattern):
    t=[0]*len(pattern);j=0
    for i in range(1,len(pattern)):
        while j>0 and pattern[i]!=pattern[j]: j=t[j-1]
        if pattern[i]==pattern[j]: j+=1
        t[i]=j
    return t
def kmp(text,pattern):
    if not pattern: return []
    t=kmp_table(pattern);j=0;matches=[]
    for i in range(len(text)):
        while j>0 and text[i]!=pattern[j]: j=t[j-1]
        if text[i]==pattern[j]: j+=1
        if j==len(pattern): matches.append(i-j+1);j=t[j-1]
    return matches
def main():
    if "--demo" in sys.argv:
        text="AABAACAADAABAABA"; pat="AABA"
        m=kmp(text,pat)
        print(f"Text: {text}\nPattern: {pat}\nMatches at: {m}")
    elif len(sys.argv)>2: print(kmp(sys.argv[1],sys.argv[2]))
if __name__=="__main__": main()
