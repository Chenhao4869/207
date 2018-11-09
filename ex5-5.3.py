def isNum(num):
    if num.isnumeric():
        return True
    elif len(num)==len(set(num)):
        return True
    else:
        return False
  
num = input("请输入字符串：")
isnum = isNum(num)
if isnum:
    print("你输入的字符串是数字！")
else:
    print("你输入的字符串不是数字！")
