Money=input("请带有符号的金额:")
if Money[-1] in ['D','d']:
    Y=6*eval(Money[0:-1])
    print("兑换后的金额是{:.2f}Y".format(Y))
if Money[-1] in ['Y','y']:
    D=eval(Money[0:-1])/6
    print("兑换后的金额是{:.2f}D".format(D))
else:
    print("输入格式错误")
