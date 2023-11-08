from User import User
from Calculator import Calculator

if __name__ == '__main__':
    user = User.Builder()   \
        .name('bsj')    \
        .email('happy@gmail.com') \
        .password('1234')   \
        .tell('010-1111-1234')  \
        .build()
    
    print(user)

    cal = Calculator(10)
    val = cal.add(10).add(10).subtract(5).divide(3).end()
    print('(10 + 10 + 10 - 5)/3 =', val)