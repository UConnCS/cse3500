# brute force longest-common-subsequence with two for-loops, return how long the longest common subsequence is
def lcs(a, b):
    max_lcs = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                max_lcs = max(max_lcs, 1 + lcs(a[i+1:], b[j+1:]))
                
    return max_lcs

if __name__ == "__main__":
    a = "ACAGGTTAC"
    b = "TCGGAATAA"
    print(lcs(a, b))