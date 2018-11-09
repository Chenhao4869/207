def multi(nums):
   
    m=1
    for i in nums:
        m=m*i
    return m
  
item_num1 = input("请输入数字，以空格分隔，若输入完成请按回车：")
item_num = item_num1.split(' ')
ls =[]
for i in item_num:
    i = eval(i)
    ls.append(i)
ans = multi(ls)
print(ans)
