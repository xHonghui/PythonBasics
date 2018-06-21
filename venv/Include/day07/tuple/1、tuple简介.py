# tuple 类型，和list 差不多，唯一不同点在于tuple 内的元素不能修改
mytuple=(1,2,3,4)
print(mytuple)
print(len(mytuple))
for  i  in mytuple:
    print(i)
for  i  in range(len(mytuple)):
    print(mytuple[i])

#mytuple[0]=10  #list可以容纳变量，tuple不可以修改内部的值
mytuple=(8,9,10,11) #
print(mytuple)
print(mytuple[:])
print(mytuple[2:3]) #默认的情况会包含最后一个