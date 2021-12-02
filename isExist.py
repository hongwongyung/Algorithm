# def isExist(source, element):
#     # return True | False

# print(isExist(['1', '2', '3', '4', '5'], '5'))

# >> True

# in 쓰지 않기
# source = ['1','6','9']
# element = '9'

def isExist(source, element):          # 함수 isExist 생성
    a = 0
    while a<len(source):          # 반복해서 비교해주기 위해 for문 생성
        if source[a] == element:        # if문을 통해 element와 source
            return True
        else:
            pass
        a=a+1
    else:
        return False

# print(isExist(source, element))
print(isExist(['1', '2', '3', '4', '5'], '2'))