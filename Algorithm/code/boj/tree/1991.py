"""
    이진 트리를 입력받아 
    전위 순회(preorder traversal), 
    중위 순회(inorder traversal), 
    후위 순회(postorder traversal) 한 결과를 출력하는 프로그램을 작성하시오.
"""


def preorder(node):    
    result.append(node) # 루트 노드를 먼저 방문 
    if tree[node][0] != '.':
        preorder(tree[node][0]) # 0 => 왼쪽 자식 
    if tree[node][1] != '.':
        preorder(tree[node][1]) # 1 => 오른쪽 자식 

def inorder(node):
    if tree[node][0] != '.':
        inorder(tree[node][0])
    result.append(node)
    if tree[node][1] != '.':
        inorder(tree[node][1])

def postorder(node):
    if tree[node][0] != '.':
        postorder(tree[node][0])
    if tree[node][1] != '.':
        postorder(tree[node][1])
    result.append(node)


N = int(input())

tree = {}

for i in range(N):
    p, l, r = input().split()
    tree[p] = (l, r)

result = []
preorder('A')
print(''.join(result))

result = []
inorder('A')
print(''.join(result))

result = []
postorder('A')
print(''.join(result))
