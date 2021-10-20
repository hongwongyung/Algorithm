n = int(input())
data = []
reseult = []

for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b))
print(data)

for i in range(n) :
    count = 0
    for j in range(n) :
        if data[i][0] < data[j][0] and data[i][1] < data[j][1] :
            count += 1 
    reseult.append(count + 1)
 
for i in reseult :
    print(i,end=' ')