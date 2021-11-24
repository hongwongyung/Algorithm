
#자료 구조 중에는 SET 이라는 자료구조가 있다. 해당 SET은 중복된 후보군을 제거해주는 데, Python의 Set 자료구조를 직접 구현해보자.

# ['a', 'p', 'p', 'l', 'e'] => ['a', 'p', 'l', 'e']
# ['1', '12', '34', '56', '56', '1'] => ['1', '12', '34', '56']

a = ['a','p','p','p','l','e']
b = [1,1,2,3]

counter = {}                             # 딕셔너리를 만들어준다.
def set(a):                              # 중복제거 할 함수 set 생성
    for i in a:                          # 반복문 for 생성 
        try: counter[i] += 1             # for문을 통해 lists의 요소를 하나씩 꺼내어 , counter라는 이름의 딕셔너리에 넣는다.
        except: counter[i] =1            # 이때 counter(딕셔너리)에 이미 존재하는 key값이라면, try문이 실행되며 value에 +1을 하게된다.
    print(list(counter.keys()))          # counter(딕셔너리)에 없는 key값이라면 except가 실행되며 value는 그냥 1로 저장된다.
                                         # key 값들만 출력

set(a)
