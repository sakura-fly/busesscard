def print_nemu():
    print("*" * 10)
    print("1、新建")
    print("2、列表")
    print("3、查询")
    print("0、退出")
    print("*" * 10)


def add(list):
    people = {}
    name = input("请输入姓名")
    people["name"] = name
    age = int(input("input age"))
    people["age"] = age
    gender = input("input gender")
    people["gender"] = gender
    list.append(people)


def list(list):
    print("姓名\t年龄\t性别")
    for l in list:
        print("%s\t%s\t%s" % (l["name"], l["age"], l["gender"]))


def find(list, name):
    for l in list:
        if l["name"] == name:
            print(l)
            is_change = input("change ? 1 = yes/other = no")
            if is_change == "1":
                update(l)
            break
    else:
        print("no name")


def update(people):
    """
    修改信息
    :param people: 要修改的信息
    """
    for k in people:
        v = input("input %s" % k)
        # 三目运算符
        # people[k] = v if v == "" else people[k]

        # 新的写法
        people[k] = v or people[k]
