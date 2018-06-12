# 输入三个点，求三角形的角度
# 求出三角形的每条边的边长，然后通过公式求角度
import math
num = eval(input("请输入数值"))
cosNum = math.cos(num);
print("cos = " + str(cosNum))
print("degrees = " + str(math.degrees(num)))
acosNum = math.acos(cosNum)
print("acos = " + str(acosNum))
print("degrees = " + str(math.degrees(acosNum)))
# 结论：abs(x) <=3 时，cos 和 acos 是相反的。目前不知道啥问题，超出了就求不回原来的那个值


