def order_coffee(coffee, *ops):
    print(coffee, ', 옵션 :', end='')
    for op in ops:
        print(op, end=' ')
    print()
    
order_coffee('아메리카노', 'tall', 'hot', '시럽추가')