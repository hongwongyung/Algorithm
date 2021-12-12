input = input()
list_input = list(map(str, input))
result = 0
a = []                      # 기재 된 문자열을 찾아서 넣을 배열
b = ''                      # 기재 된 문자열은 서로 1개로 취급 되어있어서 다시 
len_list_input = len(list_input)

for i in range(len(list_input)):
    if list_input[i] == 'c':
        if list_input[i+1] == '=':
            a.append(''.join(list_input[i:i+2]))
            b += (''.join(list_input[i:i+2]))
        elif list_input[i+1] == '-':
            a.append(''.join(list_input[i:i+2]))
            b += (''.join(list_input[i:i+2]))
    if list_input[i] == 'd':
        if list_input[i+1] == 'z':
            if list_input[i+2] == '=':
                a.append(''.join(list_input[i:i+3]))
                b += (''.join(list_input[i:i+2]))
        elif list_input[i+1] == '-':
            a.append(''.join(list_input[i:i+2]))
            b += (''.join(list_input[i:i+2]))
    if list_input[i] == 'l':
        if list_input[i+1] == 'j':
            a.append(''.join(list_input[i:i+2]))
            b += (''.join(list_input[i:i+2]))
    if list_input[i] == 'n':
        if list_input[i+1] == 'j':
            a.append(''.join(list_input[i:i+2]))
            b += (''.join(list_input[i:i+2]))
    if list_input[i] == 's':
        if list_input[i+1] == '=':
            a.append(''.join(list_input[i:i+2]))
            b += (''.join(list_input[i:i+2]))
    if list_input[i] == 'z':
        if list_input[i+1] == '=':
            a.append(''.join(list_input[i:i+2]))
            b += (''.join(list_input[i:i+2]))

len_b = len(b)
len_a = len(a)
print("입력한 문자열 총갯수", list_input)
print("a의 개수",len_a)
print("b의 개수",len_b)
print((len_list_input)-(len_b)+(len_a))


# for i in list_input:
#     if i == 'c=':
#         result += 1
#     elif i == 'c-':
#         result += 1
    