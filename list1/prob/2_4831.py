# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTLS24ao9ADFAVT
# 복습 : 0

T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    line = [0] + list(map(int, input().split()))

    count = 0
    cur = 0  # 현재 충전소의 인덱스

    while N - line[cur] > K:
        for target in range(M, cur, -1):
            if line[target] - line[cur] <= K:
                cur = target
                count += 1
                break
        else:  # 이동할 수 있는 충전소가 없음
            count = 0
            break

    print(f"#{tc} {count}")
