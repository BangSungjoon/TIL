# replace()
# 전체 문자열에서 특정 문자열을 찾아서 다른 문자열로 변경

course = 'Java Programming'

# Java 찾아서 Python으로 변경
course_replace = course.replace('Java', 'Python')
print(course_replace)

# Web 찾아서 Python으로 변경
course_replace2 = course.replace("Web", "Python")
print(course_replace2) # 못찾으면 원래 문자열 출력