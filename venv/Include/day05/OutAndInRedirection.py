# 输入输出重定向
import os
cmd = input("cmd")  # 输入
os.system(cmd)

# 执行 OutAndInRedirection.py 文件里面的内容（如上），并将输出结果输出到 1.txt 文件中
# python OutAndInRedirection.py >1.txt

# >> 表示追加内容， > 表示覆盖原有的内容的写入
# python OutAndInRedirection.py >>1.txt

# 将 2.txt 文件内容输入并指定（如上代码）
# python OutAndInRedirection.py <2.txt

# 将 2.txt 文件的内容输入并指定成功，并将结果输出到 3.txt 文件
# python OutAndInRedirection.py <2.txt>3.txt
