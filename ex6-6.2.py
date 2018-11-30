def isRepetitive(nList:list):
    for e in nList:
        if nList.count(e)>1:
            return True
        return False
    
list1 =[1,2,1,3,1,]
if isRepetitive(list1):
    print("有重复")
else:
    print("没有重复")

list2 =['china','chinese']
if isRepetitive(list2):
    print("有重复")
else:
    print("没有重复")
