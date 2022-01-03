# n = int(input())                #input값으로 숫자를 받아야 하기 때문에 int를 써준다

# for i in range(n):              #피라미드 모양을 만들어 주어야 하기 때문에 반복문인 for문을 이용해준다. range를 통해 반복 될 횟수를 정해준다.
#     for j in range(1,i+1):      #한번 더 for문을 사용해 주어서 점진적으로 *이 하나씩 늘어나도록 해준다. 그리고 range의 범위도 0이 아닌 
#                                 #1부터 설정해줌으로서 *이 하나부터 나오도록 한다.
#         print('*', end ='')     #
#     print('*')                   #

# # #반대로 점점 작아져야 한다.
# # for i in reversed(range(n-1)):
# #     for j in (range(1,i+1)):
# #         print('*', end='')
# #     print('*')

# #
# for i in range(n-1,0,-1):           # 
#     for j in range(1,i):
#         print('*', end="")
#     print('*')


a =[2,4,7,5]

for i in (a):
    if i % 2 == 0:
        print(i)
