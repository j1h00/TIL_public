def solution(n, edges):
    answer = 0

    visited = [[0]*n for _ in range(n)]
    graph = {k:[] for k in range(n)}
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)

    def paths(node):
        all_paths = []
        def dfs(now, cur_path):
            if not graph[now]:
                if cur_path not in all_paths:
                    all_paths.append(cur_path)
                return
            
            for nxt in graph[now]:
                dfs(nxt, cur_path+[now])
            return
        dfs(node, [])
        return all_paths


    return answer

answer1 = solution(5, [[0,1],[0,2],[1,3],[1,4]]	)
print(answer1)

answer2 = solution(4, [[2,3],[0,1],[1,2]])
print(answer2)
