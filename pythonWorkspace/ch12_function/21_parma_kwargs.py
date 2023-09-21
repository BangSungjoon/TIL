# 가변길이 매개변수 : **kwargs

def show_keyward(**kwargs):
    for key in kwargs.keys():
        print(key, end=' ')
    
    print('\n')

    for value in kwargs.values():
        print(value, end=' ')
    
    print('\n')

    for item in kwargs.items():
        print(item)

show_keyward(id='abcd',
             name='kim',
             phone='010-1234-1234')
print('\n')
show_keyward(id='sky',
             name='lee',
             phone='010-1234-1234',
             address='seoul')