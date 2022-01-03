# 20210702
# 2021년 07월 02일

# 20200422
# 2020년 04월 22일

# YYYYMMDD 형식의 문자열 입력 시 아래와 같이 나타내주시면 됩니다.
# 오늘부터 위처럼 YYYYMMdd 로 입력된 일까지 얼마나 D-DAY가 남았는 지 표시해주는 프로그램을 직접 작성해보는 게 좋겠습니다.

#1. 각 달의 막일에 대해서 고려하고 특히 2월 29일, 윤년을 구하는 부분도 신경써보세요.
#2. 오늘 날짜를 어떻게 구해야할 지 생각해보세요.


# print(int(now.strftime('%Y'))-10)


# 입력한 날짜
x = (input())
y = int(x[0:4])
m = int(x[4:6])
d = int(x[6:8])
in_date = ('{}년 {}월 {}일'.format(y,m,d ))
# print(in_date)

# 오늘 날짜
import datetime
now = datetime.datetime.now()
Y = (int(now.strftime('%Y')))
M = (int(now.strftime('%m')))
D = (int(now.strftime('%d')))
date = (now.strftime('{}년 {}월 {}일'.format(Y,M,D)))
# print(date)


# 날짜에서 날짜 빼기..
# d-day만들기 입력날짜 - 오늘날짜
# 1년 = 365일
# 1달 = 31일 or 30일 or 29일 or 28일
# 예) 2022년 1월 1일 - 2021년 7월 26일 = (2022*365 + 1*31 + 1) - (2021*365 + 7*30 + 26) = ? 738062
# (1,3,5,7,8,10,12)월 = 31일
# (4,6,9,11)월 = 30일
#
# 2월 = 28일
def d_day(Y,M,D,y,m,d):

    if (D-d <= 0):
        D = D-d+31
        M = M-1
    return(D)
print(('{}년 {}월 {}일'.format(Y,M,D)))


d_day(Y,M,D,y,m,d)