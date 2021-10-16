# 'c=' or 'c-' or 'dz=' or 'd-' or 'lj' or 'nj' or 's=' or 'z=' 찾기
input = (input())

for i in input:
    if input.find('c=') > -1:
        input = (input.replace("c=", "A"))
    if input.find('c-') > -1:
        input = (input.replace("c-", "A"))
    if input.find('dz=')> -1:
        input = (input.replace("dz=", "A"))
    if input.find('d-')> -1:
        input = (input.replace("d-", "A"))
    if input.find('lj')> -1:
        input = (input.replace("lj", "A"))
    if input.find('nj')> -1:
        input = (input.replace("nj", "A"))
    if input.find('s=')> -1:
        input = (input.replace("s=", "A"))
    if input.find('z=')> -1:   
        input = (input.replace("z=", "A"))

print("결과값",len(input))
