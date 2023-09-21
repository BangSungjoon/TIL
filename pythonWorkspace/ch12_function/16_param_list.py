# 함수에게 리스트 전달
# 매개변수를 리스트로 받는다. (얕은 복사)
def show_names(names):
    names[0] = 'K' # 함수 내에서 리스트 원소 변경 -> 원본도 변경됨
    print(names)

names_list = ['kim','lee','park']
show_names(names_list)
print(names_list)


# 깊은 복사 : 매개변수 값 변경해도 원본 변경되지 않음
def show_names(names):
    names = list(names) 
    names[0] = 'K' # 함수 내에서 리스트 원소 변경 -> 원본 변경되지 않음
    print(names)

names_list = ['kim','lee','park']
show_names(names_list)
print(names_list)