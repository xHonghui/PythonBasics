# if else 的另一种用法
num = 10;
price = 20 if num > 15 else 90
print(price)

# 或者
import os
shellCode = 20;
os.system("notepad") if shellCode > 30 else os.system("calc")

shellCode = 10
os.system("ipconfig") if shellCode>10 else os.system("notepad")

shellCode = 100
os.system("notepad") if shellCode>=100 else os.system("cale")