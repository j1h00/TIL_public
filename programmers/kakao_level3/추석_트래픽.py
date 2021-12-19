"""
초당 최대 처리량은 요청의 응답 완료 여부에 관계없이 
임의 시간부터 1초(=1,000밀리초)간 처리하는 요청의 최대 개수를 의미한다.

S = 2016-09-15 hh:mm:ss.sss
T = 0.1s, 0.312s, 2s (0.001 ≦ T ≦ 3.000)
예를 들어, 로그 문자열 2016-09-15 03:10:33.020 0.011s은 
"2016년 9월 15일 오전 3시 10분 33.010초"부터 "2016년 9월 15일 오전 3시 10분 33.020초"까지 
"0.011초" 동안 처리된 요청을 의미한다. (처리시간은 시작시간과 끝시간을 포함)

lines 배열은 응답완료시간 S를 기준으로 오름차순 정렬되어 있다.
solution 함수에서는 로그 데이터 lines 배열에 대해 초당 최대 처리량을 리턴한다.
"""
# 슬라이딩 윈도우 1ms 단위 => 24 * 3600 * 1000 * n * 1000ms => 불가능!
def solution(lines):
    log_time = []

    for line in lines:
        y, t, ms = line.split()
        h, m, s = t.split(':')
        ms = float(ms[:-1]) * 1000 # change to milli second 
        end_time = (int(h)*3600 + int(m)*60 + float(s)) * 1000 
        start_time = end_time - ms + 1
        log_time.append((start_time, end_time))

    answer = 0
    for i in range(len(lines)):
        cnt = 0
        cur_end_time = log_time[i][1]
        for j in range(i, len(lines)):
            start_time = log_time[j][0]
            if cur_end_time > start_time - 1000:
                cnt += 1
        answer = max(answer, cnt)
        
    return answer


lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

print(solution(lines))