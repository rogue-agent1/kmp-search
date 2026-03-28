#!/usr/bin/env python3
"""kmp_search - Knuth-Morris-Pratt string search."""
import sys
def build_lps(pattern):
    lps=[0]*len(pattern);length=0;i=1
    while i<len(pattern):
        if pattern[i]==pattern[length]:length+=1;lps[i]=length;i+=1
        elif length:length=lps[length-1]
        else:lps[i]=0;i+=1
    return lps
def search(text,pattern):
    lps=build_lps(pattern);matches=[];i=j=0
    while i<len(text):
        if text[i]==pattern[j]:i+=1;j+=1
        if j==len(pattern):matches.append(i-j);j=lps[j-1]
        elif i<len(text) and text[i]!=pattern[j]:
            if j:j=lps[j-1]
            else:i+=1
    return matches
if __name__=="__main__":
    if len(sys.argv)<3:print("Usage: kmp_search.py <pattern> <text|file>");sys.exit(1)
    pattern=sys.argv[1]
    text=open(sys.argv[2]).read() if len(sys.argv[2])>100 or "." in sys.argv[2] else sys.argv[2]
    matches=search(text,pattern);print(f"{len(matches)} matches found")
    for pos in matches[:20]:
        ctx=text[max(0,pos-20):pos+len(pattern)+20];print(f"  pos {pos}: ...{ctx}...")
