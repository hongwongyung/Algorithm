n, k = input().split()
n = int(n)
k = int(k)

def mul(n,k):
    if n % k == 0 or k % n == 0:
        print("배수이다.")
    else:
        print("배수가 아니다.")

mul(n,k)

# mul(66,22)