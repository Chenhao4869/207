from random import*
TIMES = input ("请输入你想做的测试次数")
TIMES = eval (TIMES)
my_first_choice_n=0
my_change_choice_n=0
for i in range(TIMES):
    a =("车""羊1""羊2")
    car_inDoor=choice(a)
    my_guess = choice(a)
    if car_indoor==my_guess:
        my_first_choice_n+=1
    else:
        my_change_choice_n+=1
    print("不改改变选择:{}",format(my_first_choice_n/TIMES))
    print("改变选择:{}",format(my_change_choice_n/TIMES))
