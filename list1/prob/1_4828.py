T = int(input())

for tc in range(T):
    N = int(input())

    l = list(map(int,input().split()))

    for i in range(N):
        for j in range(N-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

    print(f"#{tc+1} {l[-1]-l[0]}")