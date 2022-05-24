# 쉽게 배우는 알고리즘 - LCS 

문병로 지음 

## 최장 공통 부분 순서 LCS

> 최장 공통 부분 순서 문제는 두 문자열 X~m~ = <x~1~, x~2~, ... x~m~> 과  Y~m~ = <y~1~, y~2~, ... y~n~>두 문자열에 공통적으로 존재하는 가장 긴 부분 순서를 구한다.  영어로 Longest Common Subsequence, 줄여서 LCS 라 한다. 

LCS 문제에 존재하는 최적 부분 구조 

- x~m~ = y~n~ 이면 X~m~ 과 Y~n~ 의 LCS 의 길이는 X~m-1~ 과  Y~n-1~ 의 LCS 길이보다 1이 크다. 

  즉 (m,n) 크기 문제의 해가 (m-1, n-1) 문제의 해를 포함한다. 

- x~m~ ≠ y~n~ 이면 X~m~ 과 Y~n~ 의 LCS 길이는 X~m~ 과 Y~n-1~ 의 LCS 길이와 X~m-1~ 과 Y~n~ 의 LCS 길이 중 큰 것과 같다. 즉 (m, n) 크기 문제의 해가 (m, n-1) 크기 문제의 해와 (m-1, n) 크기 문제의 해를 포함한다. 



**재귀 호출**

```pseudocode
LCS(m, n) 
{
	if (m=0 or n=0) then return 0;
	else if (xm = ym) then return LCS(m-1, n-1) + 1;
	else return max(LCS(m-1, n), LCS(m, n-1))
}
```

**동적 프로그래밍**

```pseudocode
LCS(m, n) 
{
	for i ← 0 to m
		C[i,0] ← 0;
    for j ← 0 to n 
    	C[j,0] ← 0;
	for i ← 1 to m
		for j ← 0 to n 
			if (xi = yi) then C[i,j] ← C[i-1,j-1] + 1;
				else C[i,j] ← max{C[i-1,j], C[i,j-1])};
	return C[m,n];
}
```

- 수행시간 Θ(mn)

### boj_9251 

```python
"""
    LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 
    모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

    예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
"""
import sys

seq1 = sys.stdin.readline()[:-1]
seq2 = sys.stdin.readline()[:-1]


N = len(seq1)
M = len(seq2)

table = [[0]*(M+1) for _ in range(N+1)] # 2차원 배열 DP 이용  

# DNA sequence comparison 과 유사함. 
for i in range(1, N+1):
    for j in range(1, M+1):
        if seq1[i-1] == seq2[j-1]: # seq1 의 i 번째와, seq2 의 j 번째 문자가 같은 경우 
            table[i][j] = table[i-1][j-1] + 1 # 대각선 왼쪽 위에서 1 더해서 내려온다. 
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1]) 

print(table[N][M])
```

