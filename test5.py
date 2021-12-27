import sys
n = int(input())

for i in range(n):
    sentence = list(sys.stdin.readline().split())
    for j in sentence:
        print(j[::-1], end=" ")