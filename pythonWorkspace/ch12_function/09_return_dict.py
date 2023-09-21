def get_info():
    member = {}
    member['이름'] = input('이름 입력 : ')
    member['나이'] = input('나이 입력 : ')
    return member

print(get_info())
print(type(get_info))