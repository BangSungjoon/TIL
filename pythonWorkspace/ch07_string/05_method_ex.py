mail = input('이메일 주소를 입력 해 주세요 : ')


if (mail.find('@') == -1 or mail.find('.') == -1) or \
    (mail.find('@') > mail.find('.')) or \
        (mail.find('.') - mail.find('@') <= 1) or \
            (mail.find('@') == 0) or \
                (len(mail) - mail.index('.') <= 1) or \
                    (mail.count('@') >= 2 or (mail.count('.'))):
    print('이메일 형식이 아닙니다.')
else:
    print('이메일 형식 입니다.')

print(f'입력한 이메일 : {mail}')