def get_interest(x, y):
    return x * y / 100

deposit = int(input('예금액 입력 : '))
int_rate = float(input('이자율 입력(%) : '))
interest = int(get_interest(deposit,int_rate))

print(f'이자액 : {interest:,}원')