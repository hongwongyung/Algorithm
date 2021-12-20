n = int(input())
b = []
c = []
x = []
y = []
rank = []
rank2 = []
rank3 = []
result = []

for i in range(n):
    data = input().split()
    b.append (data)
    x.append(b[i][0])
    y.append(b[i][1])

for i in b:     
    for j in i:    
        c.append((j))

int_x = list(map(int, x)) 
int_y = list(map(int, y)) 

for i in ((int_x)):
    rank.append(1)

for i in range(len(int_x)):
    for j in range (len(int_x)):
        if int_x[i] < int_x[j]:
            rank[i] += 1

for i in range(len(int_x)):
    for j in range(len(int_x)):
        if rank[j] == i+1:
            int_x[j] = rank[j]

for i in ((int_y)):
    rank2.append(1)

for i in range(len(int_y)):
    for j in range (len(int_y)):
        if int_y[i] < int_y[j]:
            rank2[i] += 1

for i in range(len(int_y)):
    for j in range(len(int_y)):
        if rank2[j] == i+1:
           int_y[j] = rank2[j]

for i in range(len(int_y)):
    result.append(int_x[i] + int_y[i])

for i in range(len(result)):
    rank3.append(1)

for i in range(len(result)):
    for j in range (len(result)):
        if result[i] > result[j]:
            rank3[i] += 1

for i in range(len(result)):
    for j in range(len(result)):
        if rank3[j] == i+1:
            result[j] = rank3[j]

for i in range(len(result)):
    print(result[i], end=' ')