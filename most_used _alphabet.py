input = input().upper()
dict = {}

for i in input :
    try: dict[i] += 1         
    except: dict[i] = 1

key = (list(dict.keys()))
value = (list(dict.values()))
value2 = (list(dict.values()))

for i in range(1, len(value)) :
    for j in range(1, len(value)):
        if (value[j-1] > value[j]):
            value[j-1], value[j] = value[j], value[j-1]

if len(value) == 1:
    print(key[0])
elif value[-2] == value[-1]:
    print("?")
else :
    print(key[value2.index(value[-1])])