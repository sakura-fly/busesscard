from src import tools

list = []
while True:

    tools.print_nemu()
    bj = input("请选择")
    if bj == "1":
        tools.add(list)
        print(list)
    elif bj == "2":
        tools.list(list)
    elif bj == "3":
        name = input("input name")
        tools.find(list, name)
    elif bj == "0":
        print("退出")
        break
    else:
        print("err")
