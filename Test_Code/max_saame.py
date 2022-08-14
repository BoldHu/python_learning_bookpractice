def find_same():
    a = input("请输入第一个数：")
    b = input("请输入第二个数：")
    a = int(a)
    b = int(b)

    while a != b:
        if a < b:
            b = b - a
            print("b - a = ", b)
        else:
            a = a - b
            print("a - b = ", a)
    
    print("maxium is %d", a)


find_same()
