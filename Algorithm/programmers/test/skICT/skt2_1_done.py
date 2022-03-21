def solution(goods):
    n = len(goods)

    # 검색어 길이 비교를 위한 함수 
    def word_length(x):
        return len(x)

    # 모든 검색어를 담은 set 을 생성하는 함수 
    def make_set(good):
        l = len(good)
        word_set = set()
        for i in range(1, l+1):
            for j in range(l-i+1):
                word_set.add(good[j:j+i])

        return word_set

    # 각각의 goods 에 대한 word_set 을 담을 배열 
    word_sets = []
    for good in goods:
        now_word_set = make_set(good)
        word_sets.append(now_word_set)

    # 정답을 담을 배열 
    answer = []
    # 모든 word_set 을 서로 비교하면서, 겹치는 검색어는 set 에서 제거 
    for i in range(n):
        now_word_set = word_sets[i] 
        for j in range(n): 
            if i == j: # 자기 자신은 비교하지 않는다. 
                continue
            now_word_set = now_word_set - word_sets[j]

        # 최소 길이 검색어를 찾기 위한 로직
        now_answer = ""
        if now_word_set:
            min_length = len(min(now_word_set, key=word_length)) 
            min_words = []
            for word in now_word_set:
                if (len(word) == min_length):
                    min_words.append(word)
            min_words.sort() # 사전 순으로 정렬
            now_answer = " ".join(min_words)
        else:
            now_answer = "None"

        answer.append(now_answer)    
    
    return answer



    
answer1 = solution(["pencil","cilicon","contrabase","picturelist"])
print(answer1)

answer2 = solution(["abcdeabcd","cdabe","abce","bcdeab"])
print(answer2)
