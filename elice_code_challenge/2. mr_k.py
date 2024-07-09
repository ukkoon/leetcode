n, m = map(int, input().split())

array = list(map(int, input().split()))

operations = []
for _ in range(m):
    i, j, k = map(int, input().split())
    operations.append((i, j, k))

for i,j,k in operations:
    print(sorted(array[i-1:j])[k-1])
