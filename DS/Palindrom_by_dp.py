# Palindrom check by Dynamic Programming

def Palindrom(s):

    n = len(s)

# generate the 2D value to check 
    dp = [[False] * n for _ in range(n)]

# check the palindrom substring of length 1
    for i in range(n):
        dp[i][i] = True

# Check the substring of length of 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True

# Check the substring of the length of more than two
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True

# the entire string is palindrom when dp[0][n-1] is true
    return dp[0][n-1] 

# Input string
s = "malayalam"
print(f"Palindrom string to check is '{s}'=>")
print(Palindrom(s))


