# 위치 인수 / 키워드 인수
def student_info(name, age, gender):
    student = {
        'name' : name,
        'age' : age,
        'gender' : gender
    }
    return student

print(student_info(name='kim', age=20, gender='여'))
print(student_info('umm', gender='남', age=30))