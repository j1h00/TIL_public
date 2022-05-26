"""
    n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다. 
    이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램을 작성하시오.
"""
import sys
sys.setrecursionlimit(10**6)

# 재귀적으로 풀어보자 => good
# 처음엔 list slicing 으로 하였는데, 메모리 초과 뜸!!
# list 는 inorder, postorder 두 개만 관리하고, index 만 넘겨서 찾자  
# recursion limit 을 풀어줘야 한다. (boj 케이스에 depth 깊은 것이 존재)
def find_root(p_start, p_end, i_start, i_end):

    if(p_start > p_end) or (i_start > i_end): # index 가 서로 엇갈리면, 끝난거임.
        return

    root = postorder[p_end] # 현재 서브 트리에서 루트는 항상 postorder 의 마지막 인덱스 
    print(root, end=" ") # 전위 순회이므로 루트 노드 먼저 출력 

    # tree 의 inorder input 을 기준으로, 다음 subtree 의 크기를 찾는다. (정점의 개수)
    len_left = position[root] - i_start # 왼쪽 서브트리의 크기 
    len_right = i_end - position[root] # 오른쪽 서브트리의 크기 

    # postorder 과 inorder 에서 대응되는 서브트리의 크기는 서로 같으므로, len_left, len_right 이용하여 인덱스 설정
    find_root(p_start, p_start+len_left-1, i_start, i_start+len_left-1) # 왼쪽 서브트리
    find_root(p_end-len_right, p_end-1, i_end-len_right+1, i_end) # 오른쪽 서브트리 


N = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0]*(N+1)
for i in range(N):
    position[inorder[i]] = i

find_root(0, N-1, 0, N-1)

