for i in range (0,6):
    for j in range(0, 1+i) :
        print('*', end='')
    for k in range(0, 6-i):
        print('', end='')
    print()