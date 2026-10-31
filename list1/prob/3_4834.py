T = int(input())

for tc in range(T):
    N = int(input())

    count = [0] * 10

    
    nums = [int(i) for i in input()]

    for i in nums:
        count[i] += 1

    print(count)

    max_idx = 0
    for i in range(1,10):
        if count[i] >= count[max_idx]:
            max_idx = i

    print(f"#{tc+1} {max_idx} {count[max_idx]}")