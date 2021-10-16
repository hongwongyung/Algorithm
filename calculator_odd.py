# 홀수 일 시 계산 X
input = input()
list_input = list(map(str, input))
result = 0

if list_input[0] != '-':
    list_input.insert(0, '+')

rest_list = list(filter(lambda x: list_input[x] == '+' or list_input[x] == '-', range(len(list_input))))
len_rest_list = len(rest_list)

for j in range(len_rest_list):
    if j+1 < len_rest_list:
        if int(''. join(list_input[rest_list[j] : rest_list[j+1]])) % 2 == 0:
            result += int(''.join(list_input[rest_list[j] : rest_list[j+1]]))
            

    if j+1 == (len_rest_list):
        if int(''. join(list_input[rest_list[j]:])) % 2 == 0:
            result += int(''.join(list_input[rest_list[j]:]))

print(result)
