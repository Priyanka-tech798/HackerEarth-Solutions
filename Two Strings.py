N=int(input())
for i in range(N):
    s1,s2 = list(map(str,input().split(" ")))
    if sorted(s1) == sorted(s2):
        print("YES")
    else:
        print("NO")
