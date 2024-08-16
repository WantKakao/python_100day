def find_teams(n, selections):
    visited = [False] * (n + 1)
    team = [False] * (n + 1)
    result = 0

    def dfs(v):
        stack = []
        current = v
        while not visited[current]:
            visited[current] = True
            stack.append(current)
            current = selections[current]

        # 사이클이 존재하면
        if current in stack:
            cycle_start = stack.index(current)
            for item in stack[cycle_start:]:
                team[item] = True
            # for i in range(cycle_start, len(stack)):
            #     team[stack[i]] = True

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)

    for i in range(1, n + 1):
        if not team[i]:
            result += 1

    return result


# 입력 처리 및 결과 출력
T = int(input())
for _ in range(T):
    n = int(input())
    selections = [0] + list(map(int, input().split()))  # 학생 번호 1부터 시작하므로 0을 추가
    print(find_teams(n, selections))
