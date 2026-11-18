#加法函数
print("这是我的第一个 Git 项目")
def add(a, b):
    return a + b

#减法函数
def subtract(a, b):
    return a - b

#乘法函数
def multiply(a, b):
    return a * b

#除法函数
def divide(a, b):
    if b == 0:
        return "除数不能为0"
    return a / b

#主程序
while True:

    print("\n=====多功能计算器=====")
    print("1.加法")
    print("2.减法")
    print("3.乘法")
    print("4.除法")
    print("输入exit退出")

    choice = input("请选择运算:")

    if choice == "exit":
        print("计算器已退出")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("输入错误，请重新选择")
        continue

    a = float(input("请输入第一个数字："))
    b = float(input("请输入第二个数字："))

    if choice == "1":
        result = add(a, b)

    elif choice == "2":
        result = subtract(a, b)

    elif choice == "3":
        result = multiply(a, b)

    elif choice == "4":
        result = divide(a, b)

    print("计算结果：", result)

# 乘法运算
num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))

result = num1 * num2

print("乘法结果：", result)

# 除法运算
num1 = float(input("请输入被除数："))
num2 = float(input("请输入除数："))

if num2 == 0:
    print("除数不能为零")
else:
    result = num1 / num2
    print("除法结果：", result)