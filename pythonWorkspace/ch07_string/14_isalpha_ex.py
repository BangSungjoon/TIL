a = input('문장을 입력하세요 : ')
alpha = num = space = abc = 0

for i in a:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        num += 1
    elif i.isspace():
        space += 1
    else:
        abc += 1

#  꼭 리스트로 안 만들어도 됨!
# my_list = list(a)
# for list in my_list:
#     if list.isalpha():
#         alpha += 1
#     elif list.isdigit():
#         num += 1
#     elif list.isspace():
#         space += 1
#     else:
#         abc += 1

print('알파벳 : ', alpha, '개')
print('숫자 : ', num, '개')
print('스페이스 : ', space, '개')
print('기타 : ', abc, '개')