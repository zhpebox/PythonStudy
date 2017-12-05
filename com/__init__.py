#!/usr/bin/python3
print("你好！");
#注释
print("The world");

if 1==1:
    print("yes!");
else:
    print("NO!");

total = 1 + 2 + \
    3;

print(total);

total = ['1','3',
         '5']

print(total);

print(r"this is an unicode Stri\nng");

#input("\n\n按下回车后 推出。");


import sys; x = 'rr' ; sys.stdout.write(x+'\n');

import sys
print("python import mode");
print("命令行参数为");
for i in sys.argv:
    print(i)
print("\n python 路径为",sys.path);