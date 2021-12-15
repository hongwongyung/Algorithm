import re

input = input()                             # 입력 받는값 input 생성
list_input = list(map(str, input))          # 입력 받은값을 list로 만들어준다.
split_input = re.split(r"-|\+", input)
plus_arr = []
minus_arr = []
result = 0

if split_input[0] == '':
    del split_input[0]
    print(split_input)

if list_input[0] == '-' :
    pass
else :
    list_input.insert(0,'+')

rest_list = list(filter(lambda x: list_input[x] == '+' or list_input[x] == '-', range(len(list_input))))

for i in range(len(split_input)):
    if list_input[rest_list[i]] == '+':
        plus_arr.append(split_input[i])
    else :
        minus_arr.append(split_input[i])

plus_arr = list(map(int, plus_arr))
minus_arr = list(map(int, minus_arr))

result += sum(plus_arr)
result -= sum(minus_arr)

print("결과값", result)
