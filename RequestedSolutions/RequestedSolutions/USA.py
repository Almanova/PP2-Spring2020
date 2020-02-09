a = int(input())
initial = {}
votes = {}
res = {}

for i in range (a):
    state, points = input().split()
    votes[state] = {}
    initial[state] = points

a = int(input())

for i in range (a):
    state, canditate = input().split()
    res[canditate] = 0
    if canditate in votes[state]:
        votes[state][canditate] = int(votes[state][canditate]) + 1
    else:
        votes[state][canditate] = 1

ans = {}

for s, k in votes.items():
    maxi = 0
    for c, p in sorted(k.items()):
        if p > maxi:
            ans[s] = c
            maxi = p

for s, c in ans.items():
    res[c] = res[c] + int(initial[s])

for c, v in sorted(res.items(), key = lambda x: (-x[1], x[0])):
    print (c, v)