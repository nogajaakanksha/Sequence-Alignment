def alpha(x,y):
    alphas = [[0,110,48,94],[110,0,118,48],[48,118,0,110],[94,48,110,0]]
    keys = {"A":0, "C":1, "G":2, "T":3}
    return alphas[keys[x]][keys[y]]

delta = 30

def populateDP(x, y):
    m = len(x)+1
    n = len(y)+1

    DP = [[0 for i in range(n)] for j in range(m)]

    for i in range(1, m):
        DP[i][0] = i*delta

    for j in range(1, n):
        DP[0][j] = j*delta

    for i in range(1, m):
        for j in range(1, n):
            mismatch = DP[i - 1][j - 1] + alpha(x[i-1], y[j-1])
            insert = DP[i][j - 1] + delta
            delete = DP[i - 1][j] + delta
            DP[i][j] = min(mismatch, insert, delete)

    return DP

def find_alignment(dp,string1, string2):
    align1=""
    align2=""
    i=len(string1)
    j=len(string2)
    while i>0 or j>0:
      if i>0 and j>0 and dp[i][j] == dp[i-1][j-1] + alpha(string1[i-1],string2[j-1]):
          align1+=string1[i-1]
          align2+=string2[j-1]
          i-=1
          j-=1

      elif i>0 and dp[i][j] == dp[i-1][j] + delta:
          align1+=string1[i-1]
          align2+="_"
          i-=1

      elif j>0 and dp[i][j] == dp[i][j-1] + delta:
          align1+="_"
          align2+=string2[j-1]
          j-=1
    return dp[len(string1)][len(string2)], align1[::-1], align2[::-1]

def needleman(string1, string2):
  DP = populateDP(string1, string2)
  return find_alignment(DP, string1, string2)
