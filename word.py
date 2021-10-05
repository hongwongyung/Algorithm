#n개의 영문 문자열이 주어진다.
#n개의 영문 문자열 모두가 끝말잇기가 이어질 때
# 입출력 예시
# 3
# apple
# elapse
# extend
# 통과

# 5
# hello
# offer
# random
# mention
# moment
# 실패

num = int(input())
def word (num):
        # 몇 번 영문 문자열을 받아줄지 숫자 넣는 input 생성
    a=[]
    for i in range(num):    # 영문 문자열을 몇 번 넣어줄지 반복해주는 for문 생성
        b = input()         # 영문 문자열을 받아주는 input 생성
        a.append(b)     # append사용으로 차례대로 a리스트에 삽입.

    for q in range(num-1):      # for문을 통해서 문자열의 끝과 처음이 같은지 반복해서 검사해준다. range로 몇 번 검사할지 횟수를 정해주게 된다.
        if (a[q][-1]) != (a[q+1][0]):
            return ("실패")
    return ("성공")
    
print(word(num))