def print_2d_arr(arr):
    for row in arr:
        for e in row:
            print("  %d" % e, end='')
        print()


def snail(arr):
    print("== start sanil ==")

    size = len(arr)
    tail = pow(size, 2) 

    max_x = size - 1
    max_y = size - 1
    min_x = 0
    min_y = 0

    x = 0
    y = 0
    # arrow = ['r', 'b', 'l', 't']
    head = 1
    turn_point = 4

    def turn_head():
        nonlocal head, turn_point, min_x, min_y, max_x, max_y

        if head == 1:
            min_x += 1

        elif head == 2:
            max_y -= 1

        elif head == 3:
            max_x -= 1

        elif head == 4:
            min_y += 1
            head = 0
            
        head += 1    

        # head += 1
        # if head == turn_point:
        #     min_x += 1
        #     min_y += 1
        #     max_x -= 1
        #     max_y -= 1
        # elif head > turn_point:
        #     head = 1

        print(x, y)
        print("HEAD: %d" % head)

    def handle():
        nonlocal x, y, head, max_y, max_y

        if head == 1:
            if y < max_y:
                y+=1
            else:
                turn_head()
                handle()
        elif head == 2:
            if x < max_x:
                x+=1
            else:   
                turn_head()
                handle()
        elif head == 3:
            if y > min_y:
                y-=1
            else:   
                turn_head()
                handle()
        elif head == 4:
            if x > min_x:
                x-=1
            else:   
                turn_head()
                handle()
        else:
            raise Exception("raise ArrowException. Given %d" % direction)

    for count in range(1, tail+1):
        arr[x][y] = count
        if count == tail:
            break
        handle()


    print("== end sanil ==")


if __name__ == "__main__":
    num = int(input("INPUT POSITIVE INTEGER NUMBER:\n"))

    print("INPUTED: %d" % num)
    tdarr = [[0]*num for _ in range(0, num)] # two dimension arr
    print_2d_arr(tdarr)

    snail(tdarr)
    print_2d_arr(tdarr)
