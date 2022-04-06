# GCF + ACDEB를 계산한다고 할 때, 
# A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 
# 두 수의 합은 99437이 되어서 최대가 될 것이다.
# 그리디 알고리즘...

N = int(input())

alphabets = {}
words = []
for i in range(N):
    words.append(input())

for word in words:
    l = len(word)
    for i in range(l):
        num = 10 ** (l - i - 1)
        alphabets[word[i]] = alphabets.get(word[i], 0) + num

answer = 0
sorted_alphabets = sorted(alphabets.values(), reverse=True)
for i in range(len(alphabets.values())):
    answer += sorted_alphabets[i] * (9-i)

print(answer)




    