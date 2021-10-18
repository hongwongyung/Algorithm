input = range(1,10001)
x = []
y = []
for i in input:
    a = list(str(i))
    b = sum(list(map(int, a))) + i
    x.append(b)
    y.append(i)

for i in y:
    if i not in x :
        print(i)