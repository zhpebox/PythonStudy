# import random
# num = random.randint(0,100)
# print(num)
#
# if num > 0:
#     for i in range(2,num):
#         print(i)
#         if (num%i) == 0:
#             print("{0}是不是质数，能被{1}整除".format(num,i))
#             break
#     else:
#         print(i)
#         print(num,"是质数")

# 定义函数
def add(x,y):
    return x+y
def sub(x,y):
    return x-y

choice = int(input("请输入1+2-"))

num1 = int(input("输入第一个数"))
num2 = int(input("输入第二个数"))

if choice == 1:
    print("{0}+{1}={2}".format(num1,num2,num1+num2))
elif choice ==2:
    print("{0}-{1}={2}".format(num1, num2, num1 - num2))