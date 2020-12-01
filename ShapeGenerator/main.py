# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

SANDS = 4

def draw_down_triangle(num):
    space=''
    while True:
        print(space,end='')
        for index in range(num):
            print('*',end=' ')
        print()
        num = num-2
        space+='  '
        if num < 0:
            break

def draw_full_triangle(num):
    space = ''
    opt = -1
    temp = num
    stop = False
    while True:
        if temp > 0:
            print(space, end='')
        for index in range(temp):
            print('*', end=' ')
        if temp > 0:
            print()
        if stop:
            break
        temp = temp + ( 2 * opt)
        if opt < 0:
            space += '  '
        else:
            space = space[:-2]
        if temp < 1:
            opt = 1
        if temp == num:
            stop = True

def start():
    data=int(input('Input num to start.'))
    draw_down_triangle(data)
    print('-------')
    draw_full_triangle(data)
    print('-------')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
