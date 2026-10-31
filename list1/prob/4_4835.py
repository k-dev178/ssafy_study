T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    l = list(map(int,input().split()))

    prefix = []
    for i in range(N-M+1):
        sum_i = 0

        for j in range(M):
            sum_i += l[i+j]

        prefix.append(sum_i)

    prefix.sort()
    print(f"#{tc+1} {prefix[-1]-prefix[0]}")