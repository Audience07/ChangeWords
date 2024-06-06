from pathlib import Path
import os

FileName = "这里填入文件路径"
OriginString = "这里填入要修改的内容"
NewString = "这里填入新的内容"
#在修改时,需要考虑到会不会在修改“The”时将原本的“Then”,“There”修改掉,所以最好在要修改的字符后面加上空格
#不支持中文


#传入Path类,文件名有效返回修改后的字符串,无效返回0

#向Path类传入文件字符串
path = Path(FileName)
Contents = ""

#捕获找不到文件报错
try:
    for line in path.read_text().splitlines():
        Contents += line.replace(OriginString,NewString)
except FileNotFoundError:
    print(f'找不到文件{path.name}')
    os._exit(0)

print(Contents)
path.write_text(Contents)
print("修改成功")


