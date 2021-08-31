# r g b
# 0~2

r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
i = 0

for r1 in range(r):
    for g1 in range(g):
        for b1 in range(b):
            print(r1, g1, b1)
            i += 1
print(i)