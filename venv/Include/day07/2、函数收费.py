# 函数收费
import os

# 备份函数
block_os_system = os.system


def function_charge(shell_str):
    if shell_str.find("a") != -1:  # 已缴费，正常执行
        block_os_system(shell_str)
    else:
        print("该用户未交费，请交费后重试")


os.system = function_charge
os.system("calc")
