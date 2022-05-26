import sys

def main():
    sys.stdin = open('input.txt')

    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        bus_stop = [0]*5001
        for _ in range(N):
            start, end = map(int, input().split())
            for i in range(start, end+1):
                bus_stop[i] += 1

        P = int(input())
        result = []
        for j in range(P):
            C = int(input())
            result.append(bus_stop[C])


        print(f'#{tc}', end = " ")
        print(*result)
main()

