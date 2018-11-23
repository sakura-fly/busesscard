bj = -1
while bj != 0:
    print("*" * 10)
    print("1、新建")
    print("2、列表")
    print("3、查询")
    print("0、退出")
    print("*" * 10)
    bj = int(input("请选择"))
    if bj == 1:
        print("1")
    elif bj == 2:
        print(2)
    elif bj == 0:
        print("退出")
    else:
        print("err")
