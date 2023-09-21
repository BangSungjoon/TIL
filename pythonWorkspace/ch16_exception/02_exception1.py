# 예외 처리
# except : 예외유형 (예외 유형 생략하는 경우)
# 에러가 발생하기만 하면 except 블록 수행

try :
    print(10/0) # 0으로 나누기 : 에러 발생
except:
    # 에러 발생 시 수행되는 구문
    print('예러 예외 처리')

try :
    print('나이 : ' + 23 + '살 ')
except:
    # 에러 발생 시 수행되는 구문
    print('예러 예외 처리')

# 예외 유형 지정
# Exception 최상위 유형
try :
    print(10/0)
except ZeroDivisionError:
    # 에러 발생 시 수행되는 구문
    print('예러 예외 처리')

try :
    print(10/0)
except Exception:
    # 에러 발생 시 수행되는 구문
    print('예러 예외 처리')


# 여러 개의 예외 처리
# 주의! : 첫 번째 에러만 처리됨
a = [1, 2, 3]
try:
    print(10/0) # 첫 번째 에러를 만나면 해당 예외 처리 구문으로 이동
    print(a[4]) # 이때 이 문장은 수행되지 않음
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다') # 얘만 처리됨
except IndexError:
    print('인덱스 범위를 벗어났습니다')


# 여러 개의 예외 처리 : 함께 처리
# 오류 메세지 확인 : as e
# 첫 번째 에러에 대한 예외 처리만 수행
try:
    print(10/0)  # ZeroDivisionError
    print(a[4])  # NameError: name 'a' is not defined
except (ZeroDivisionError, IndexError) as e:
    print('오류가 발생했습니다', e)

# 최상위 Exception으로 예외 처리
try:
    print(a[4])
    print(10/0)
except Exception as e:
    print('오류가 발생했습니다', e)