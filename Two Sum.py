num = list(map(int,input().split()))
target = int(input())
ans = []
for x in num:
    temp = target-x
    if temp in num:
        ans.append(num.index(x))
        ans.append(num.index(temp))
        print(ans)
        break