def get_names() :
    member = []
    for i in range (3):
        name = input('이름 입력 : ')
        member.append(name)
    return member

result = get_names()
print(result)  
print(type(result))